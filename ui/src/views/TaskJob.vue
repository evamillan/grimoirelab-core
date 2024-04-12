<template>
  <div class="mt-4">
    <v-card v-if="job.status" :class="'border-' + job.status" class="pa-2" variant="outlined">
      <v-card-title class="text-subtitle-2 pb-0">
        Job {{ $route.params.jobid }}
        <v-chip :color="job.status" class="ml-3" density="comfortable" size="small">
          {{ job.status }}
        </v-chip>
      </v-card-title>
      <v-card-subtitle>
        {{ new Date(job.ended_at).toLocaleString() }}
      </v-card-subtitle>
      <div v-if="job.result" class="pl-4 mt-2">
        <p class="text-body-2 mb-2">
          Fetched
          <span class="font-weight-medium">
            {{ job.result.fetched }}
          </span>
        </p>
        <p class="text-body-2 mb-2">
          Skipped
          <span class="font-weight-medium">
            {{ job.result.skipped }}
          </span>
        </p>
      </div>
    </v-card>
    <div v-if="job.log" class="mt-4">
      <code v-for="(log, index) in job.log" :key="index">
        {{ new Date(log.created * 1000).toLocaleString('en-us') }} [{{ log.module }}] {{ log.msg }}
      </code>
    </div>
  </div>
</template>
<script>
import { API } from '@/services/api'
export default {
  data() {
    return {
      job: {}
    }
  },
  methods: {
    async fetchJob(id) {
      const response = await API.scheduler.getJob(id)
      if (response.data) {
        this.job = response.data
      }
    }
  },
  mounted() {
    this.fetchJob(this.$route.params.jobid)
  }
}
</script>
<style lang="scss" scoped>
@import './../assets/cards.scss';
code {
  display: block;
  background-color: rgb(var(--v-theme-on-surface));
  color: rgb(var(--v-theme-surface), var(--v-medium-emphasis-opacity));
  padding: 4px 1rem;
  font-size: 0.8rem;
  white-space: pre-wrap;

  &:first-child {
    padding-top: 1rem;
  }
  &:last-child {
    padding-bottom: 1rem;
  }
}
</style>
