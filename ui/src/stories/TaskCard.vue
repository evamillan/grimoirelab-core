<template>
  <v-card
    :class="'border-' + status"
    class="pa-2 pb-4"
    variant="outlined"
  >
    <v-row>
      <v-col cols="6">
        <v-card-title>
          {{ id }}
        </v-card-title>
        <v-card-subtitle class="pb-2">
          <v-icon size="small" start>
            {{ 'mdi-' + backend }}
          </v-icon>
          <span class="font-weight-medium">
            {{ category }}
          </span>
          <span v-if="backendArgs?.uri">
            from {{ backendArgs.uri }}
          </span>
        </v-card-subtitle>
        <v-card-subtitle>
          <v-icon
            :aria-label="status"
            :color="status"
            role="img"
            aria-hidden="false"
            size="small"
            start
          >
            {{ statusIcon }}
          </v-icon>
          Last run {{ lastExecution }}
        </v-card-subtitle>
      </v-col>
      <v-divider class="mt-2" vertical></v-divider>
      <v-col cols="6" class="px-4 py-6 mt-2">
        <p class="pb-2 text-body-2">
          <v-icon color="medium-emphasis" size="small" start>
            mdi-calendar
          </v-icon>
          Scheduled for 
          <span class="font-weight-medium">
            {{ scheduledDate }}
          </span>
        </p>
        <p class="pb-2 text-body-2">
          <v-icon color="medium-emphasis" size="small" start>
            mdi-timelapse
          </v-icon>
          Every
          <span class="font-weight-medium">
            {{ interval }}
          </span>
          minutes
        </p>
        <p class="text-body-2">
          <v-icon color="medium-emphasis" size="small" start>
            mdi-arrow-u-right-top
          </v-icon>
          <span class="font-weight-medium">
            {{ maxRetries }}
          </span>
          max retries
        </p>
      </v-col>
    </v-row>
  </v-card>
</template>
<script>
export default {
  name: "TaskCard",
  props: {
    age: {
      type: [Number, String],
    },
    backend: {
      type: String,
    },
    backendArgs: {
      type: Object
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
    interval: {
      type: [Number, String],
    },
    scheduledDate: {
      type: String,
    },
    lastExecution: {
      type: String,
    },
    maxRetries: {
      type: [Number, String],
    },
  },
  computed: {
    statusIcon() {
      switch (this.status) {
        case "finished":
          return "mdi-check";
        case "failed":
          return "mdi-close";
        case "running":
          return "mdi-sync";
        default:
          return "mdi-calendar";
      }
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
</style>