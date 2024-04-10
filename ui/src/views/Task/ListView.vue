<template>
  <v-container>
    <task-list
      :tasks="tasks"
      :count="count"
      :pages="pages"
      @create="createTask($event)"
      @delete="deleteTask($event)"
      @reschedule="rescheduleTask($event)"
      @update:page="fetchTasks($event)"
    />
    <v-snackbar v-model="snackbar.open" :color="snackbar.color">
      {{ snackbar.text }}
    </v-snackbar>
  </v-container>
</template>
<script>
import { API } from '@/services/api'
import TaskList from '@/components/TaskList/TaskList.vue'

export default {
  components: { TaskList },
  data() {
    return {
      tasks: [],
      pages: 1,
      currentPage: 1,
      count: 0,
      snackbar: {
        open: false,
        color: 'success',
        text: ''
      }
    }
  },
  mounted() {
    this.fetchTasks(1)
  },
  methods: {
    async createTask(formData) {
      try {
        const response = await API.scheduler.create(formData)
        Object.assign(this.snackbar, {
          open: true,
          color: 'success',
          text: response.data.message
        })
        this.fetchTasks(this.currentPage)
      } catch (error) {
        Object.assign(this.snackbar, {
          open: true,
          color: 'error',
          text: error.response?.data?.message || error
        })
      }
    },
    async deleteTask(taskId) {
      try {
        await API.scheduler.delete(taskId)
        Object.assign(this.snackbar, {
          open: true,
          color: 'success',
          text: `Deleted task ${taskId}`
        })
        this.fetchTasks(this.currentPage)
      } catch (error) {
        Object.assign(this.snackbar, {
          open: true,
          color: 'error',
          text: error.response?.data?.message || error
        })
      }
    },
    async fetchTasks(page = 1) {
      try {
        const response = await API.scheduler.list({ page })
        if (response.data.objects) {
          this.tasks = response.data.objects
          this.count = response.data.count
          this.pages = response.data.num_pages
          this.currentPage = response.data.current_page
        }
      } catch (error) {
        console.log(error)
      }
    },
    async rescheduleTask(taskId) {
      try {
        await API.scheduler.reschedule(taskId)
        Object.assign(this.snackbar, {
          open: true,
          color: 'success',
          text: `Rescheduled task ${taskId}`
        })
        this.fetchTasks(this.currentPage)
      } catch (error) {
        Object.assign(this.snackbar, {
          open: true,
          color: 'error',
          text: error.response?.data?.message || error
        })
      }
    }
  }
}
</script>
