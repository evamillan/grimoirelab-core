# -*- coding: utf-8 -*-
#
# Copyright (C) GrimoireLab Contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#     Jose Javier Merchante <jjmerchante@bitergia.com>
#

import json
import pickle

import django_rq

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from rq.exceptions import NoSuchJobError
from rq.job import Job

from .errors import NotFoundError
from .models import FetchTask
from .scheduler import (schedule_task,
                        remove_task,
                        reschedule_task as scheduler_reschedule_task)
from .common import Q_DEFAULT_JOBS


@require_http_methods(["GET"])
def list_tasks(request):
    tasks = FetchTask.objects.all()

    page_number = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 10)
    paginator = Paginator(tasks, per_page=per_page)
    page_obj = paginator.get_page(page_number)

    serialized_tasks = [
        {
            'id': task.id,
            'backend': task.backend,
            'category': task.category,
            'backend_args': task.backend_args,
            'status': task.get_status_display(),
            'age': task.age,
            'executions': task.executions,
            'num_failures': task.num_failures,
            'job_id': task.job_id,
            'queue': task.queue,
            'scheduled_datetime': task.scheduled_datetime,
            'interval': task.interval,
            'max_retries': task.max_retries,
            'last_execution': task.last_execution,
            'task_id': task.task_id,
        }
        for task in page_obj
    ]

    return JsonResponse({
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'objects': serialized_tasks
    })


@require_http_methods(["GET"])
def show_job(request, job_id):
    queue = django_rq.get_queue(Q_DEFAULT_JOBS)
    connection = queue.connection

    try:
        job = Job.fetch(job_id, connection=connection)
    except NoSuchJobError:
        return JsonResponse({'error_message': f'Job {job_id} not found'}, status=404)

    response = {
        "created_at": job.created_at,
        "started_at": job.started_at,
        "ended_at": job.ended_at,
        "worker_name": job.worker_name,
        "queue": job.origin,
        "func_name": job.func_name,
        "args": job.args,
        "kwargs": job.kwargs,
        "enqueued_at": job.enqueued_at,
        "status": job.get_status(),
        "log": None,
        "result": None,
    }
    if 'log' in job.meta:
        response['log'] = job.meta['log']

    if 'result' in job.meta:
        response['result'] = job.meta['result'].to_dict()

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_task(request, task_id):
    try:
        task = FetchTask.objects.get(task_id)
    except FetchTask.DoesNotExist:
        return JsonResponse({"error": "Task not found."}, status=404)

    response = {
        'id': task.id,
        'backend': task.backend,
        'category': task.category,
        'backend_args': task.backend_args,
        'status': task.get_status_display(),
        'age': task.age,
        'executions': task.executions,
        'num_failures': task.num_failures,
        'job_id': task.job_id,
        'queue': task.queue,
        'scheduled_datetime': task.scheduled_datetime,
        'interval': task.interval,
        'max_retries': task.max_retries,
        'last_execution': task.last_execution,
        'task_id': task.task_id,
    }

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_task(request):
    task_args = {}
    task_data = json.loads(request.body)['taskData']
    task_args['backend'] = task_data['backend']
    task_args['category'] = task_data['category']
    task_args['backend_args'] = {}
    if task_data['backend'] == 'git':
        task_args['backend_args']['uri'] = task_data['backendArgs']['uri']
        task_args['backend_args']['gitpath'] = settings.GIT_PATH
        if 'fromDate' in task_data['backendArgs']:
            task_args['backend_args']['from_date'] = task_data['backendArgs']['fromDate']

    if 'interval' in task_data['schedulerArgs']:
        task_args['interval'] = int(task_data['schedulerArgs']['interval'])
    if 'maxRetries' in task_data['schedulerArgs']:
        task_args['max_retries'] = int(task_data['schedulerArgs']['maxRetries'])

    task = schedule_task(**task_args)

    return JsonResponse({'status': 'ok',
                         'message': f"Task {task.id} added correctly"}, safe=False)


@require_http_methods(["POST"])
def delete_task(request):
    task_id = json.loads(request.body)['taskId']

    try:
        remove_task(task_id)
    except NotFoundError:
        err = "Task not found"
        return JsonResponse({'status': 'false', 'message': err}, status=404)
    return JsonResponse({'status': 'ok',
                         'message': "Task removed correctly"}, safe=False)


@require_http_methods(["POST"])
def reschedule_task(request):
    task_id = json.loads(request.body)['taskId']

    try:
        rescheduled = scheduler_reschedule_task(task_id)
    except NotFoundError:
        err = "Task not found"
        return JsonResponse({'status': 'false', 'message': err}, status=404)

    if not rescheduled:
        err = "Error rescheduling the task"
        return JsonResponse({'status': 'false', 'message': err},
                            status=400)
    return JsonResponse({'status': 'ok',
                         'message': "Task rescheduled correctly"})


def create_job(request):
    backend = 'git'
    category = 'commit'
    backend_args = {
        "gitpath": "/tmp/git/arthur.git/",
        "uri": "https://github.com/chaoss/grimoirelab-kingarthur.git"
    }

    task = schedule_task(backend=backend,
                         category=category,
                         backend_args=backend_args)

    return JsonResponse({'task': task.task_id})


def list_jobs(request):
    queue = django_rq.get_queue(Q_DEFAULT_JOBS)
    connection = queue.connection

    def job_info(jid):
        job = Job.fetch(id=jid, connection=connection)
        return job.exc_info

    def job_sched_info(jid):
        job = Job.fetch(id=jid, connection=connection)
        return job.kwargs

    def job_result(jid):
        job = Job.fetch(id=jid, connection=connection)
        data = job.to_dict()
        data['data'] = pickle.loads(job.data)
        data['result'] = job.result.to_dict()
        data['meta'] = job.meta
        return data

    out = {
        'started': {jid: job_info(jid) for jid in queue.started_job_registry.get_job_ids()},
        'scheduled': {jid: job_sched_info(jid) for jid in queue.scheduled_job_registry.get_job_ids()},
        'failed': {jid: job_info(jid) for jid in queue.failed_job_registry.get_job_ids()},
        'deferred': {jid: job_info(jid) for jid in queue.deferred_job_registry.get_job_ids()},
        'canceled': {jid: job_info(jid) for jid in queue.canceled_job_registry.get_job_ids()},
        'finished': {jid: job_result(jid) for jid in queue.finished_job_registry.get_job_ids()},
    }

    return JsonResponse(out)


def clear_jobs(request):
    queue = django_rq.get_queue(Q_DEFAULT_JOBS)

    registries = [
        queue.failed_job_registry,
        queue.finished_job_registry,
        queue.scheduled_job_registry,
        queue.started_job_registry,
        queue.canceled_job_registry,
        queue.deferred_job_registry
    ]
    for registry in registries:
        for jid in registry.get_job_ids():
            registry.remove(jid)

    return JsonResponse({'removed': True})
