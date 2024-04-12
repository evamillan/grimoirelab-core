<template>
  <div>
    <h2 class="text-h6 mb-4">
      Jobs
      <v-chip class="ml-2" density="comfortable">
        {{ jobs.length }}
      </v-chip>
    </h2>
    <status-card
      v-for="job in jobs"
      :key="job.job_id"
      :status="job.job_status"
      :to="{
        name: 'job',
        params: { jobid: job.job_id }
      }"
      class="mb-2"
    >
      <v-card-title class="text-subtitle-2">
        {{ job.job_id }}
        <v-chip :color="job.job_status" class="ml-3" density="comfortable" size="small">
          {{ job.job_status }}
        </v-chip>
      </v-card-title>
    </status-card>
  </div>
</template>
<script>
import StatusCard from '@/components/StatusCard.vue'

export default {
  name: 'JobList',
  components: { StatusCard },
  props: {
    jobs: {
      type: Array,
      required: true
    }
  }
}
</script>
