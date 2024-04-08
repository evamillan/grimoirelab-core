<template>
  <v-card
    :class="'border-' + status"
    :to="{
      name: 'task',
      params: { id: id }
    }"
    variant="outlined"
  >
    <v-row>
      <v-col cols="6">
        <v-card-title class="text-subtitle-2 pb-0 d-flex align-center">
          {{ id }}
          <!-- <v-chip :color="status" class="ml-3" density="compact" size="small">
            {{ status }}
          </v-chip> -->
          <div class="ml-auto">
            <v-tooltip v-for="job in jobs" :text="job.status" location="bottom">
              <template v-slot:activator="{ props }">
                <v-icon v-bind="props" :color="job.status">
                  mdi-square
                </v-icon>
              </template>
            </v-tooltip>
          </div>
        </v-card-title>
        <v-card-subtitle class="font-weight-medium">
          <v-icon
            :aria-label="backend"
            role="img"
            aria-hidden="false"
            size="small"
          >
            {{ 'mdi-' + backend }}
          </v-icon>
          {{ category }}
        </v-card-subtitle>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="5" class="px-4 py-6">
        <p class="pb-2 text-body-2">
          <v-icon color="medium-emphasis" size="small" start>
            mdi-format-list-numbered
          </v-icon>
          <span class="font-weight-medium">
            {{ executions }}
          </span>
          executions
        </p>
        <p class="text-body-2">
          <v-icon color="medium-emphasis" size="small" start>
            mdi-calendar
          </v-icon>
          {{ lastExecution }}
        </p>
      </v-col>
      <v-col class="mx-4 py-6 d-flex flex-column align-end">
        <v-btn
          icon="mdi-delete"
          color="danger"
          variant="text"
          size="small"
          density="comfortable"
          @click.stop.prevent
        />
        <v-btn
          icon="mdi-refresh"
          variant="text"
          size="small"
          density="comfortable"
          @click.stop.prevent
        />
      </v-col>
    </v-row>
  </v-card>
</template>
<script>
export default {
  name: 'TaskListItem',
  props: {
    backend: {
      type: String,
    },
    category: {
      type: String,
    },
    status: {
      type: String,
    },
    executions: {
      type: [Number, String]
    },
    id: {
      type: String,
    },
    scheduledDate: {
      type: String,
    },
    lastExecution: {
      type: String,
    },
    jobs: {
      type: Array
    }
  },
};
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