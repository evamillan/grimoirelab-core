<template>
  <v-container>
    <task-card
    :age="task.age"
    :backend="task.backend"
    :backend-args="task.backendArgs"
    :category="task.category"
    :status="task.status"
    :executions="task.executions"
    :id="task.id"
    :interval="task.interval"
    :last-execution="task.lastExecution"
    :max-retries="task.maxRetries"
    :scheduled-date="task.scheduledDate"
    class="mt-4"
  />
  <router-view></router-view>
  </v-container>
</template>
<script>
import TaskCard from './../stories/TaskCard.vue';

export default {
  name: 'Task',
  components: { TaskCard },
  data() {
    return {
      task: {
        backend: "github",
        category: "commits",
        status: "finished",
        executions: 8,
        id: "cdfgh5678",
        scheduledDate: "2024-03-27",
        lastExecution: "2024-03-20",
        interval: 5000,
        maxRetries: 5,
        age: 1,
        backendArgs: {
          uri:"https://github.com/chaoss/grimoirelab-kingarthur.git"
        },
      },
    }
  }
}
</script>