<template>
  <div class="mt-4">
    <h2 class="text-h6 mb-4">
      Jobs
      <v-chip class="ml-2" density="comfortable">
        {{ jobs.length }}
      </v-chip>
    </h2>
    <v-card
      v-for="job in jobs"
      :class="'border-' + job.status"
      :to="{
        name: 'job',
        params: { jobid: job.id }
      }"
      class="mb-2"
      variant="outlined"
    >
      <v-card-title class="text-subtitle-2">
        {{ job.id }}
        <v-chip :color="job.status" class="ml-3" density="compact" size="small">
          {{ job.status }}
        </v-chip>
      </v-card-title>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      jobs: [
          {
            id: "1234567890",
            status: "finished"
          },
          {
            id: "0987654321",
            status: "failed"
          }
        ]
    }
  }
}
</script>
<style lang="scss" scoped>
.v-card--variant-outlined {
  background: rgb(var(--v-theme-surface));
  border: thin solid rgba(0, 0, 0, 0.08);
  border-left: 6px solid rgb(var(--v-border-color));
}

.v-chip.v-chip--density-compact {
  height: calc(var(--v-chip-height) + -6px);
}
</style>