import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      // redirect: '/tasks'
    },
    {
      path: '/tasks',
      name: 'tasks',
      meta: {
        breadcrumb: {
          title: "Tasks",
          to: { name: 'tasks' }
        }
      },
      redirect: {
        name: 'taskList'
      },
      children: [
        {
          path: '',
          name: 'taskList',
          component: () => import('../views/TaskList.vue')
        },
        {
          path: ':id',
          name: 'task',
          meta: {
            breadcrumb: {
              title: 'Task',
              param: 'id',
            }
          },
          redirect: {
            name: 'taskJobs'
          },
          component: () => import('../views/Task.vue'),
          children: [
            {
              name: 'taskJobs',
              path: '',
              component: () => import('../views/TaskJobs.vue'),
            },
            {
              name: 'job',
              path: 'job/:jobid',
              component: () => import('../views/TaskJob.vue'),
              meta: {
                breadcrumb: {
                  title: 'Job',
                  param: 'jobid'
                }
              },
            }
          ]
        },
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
