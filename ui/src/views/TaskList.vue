<template>
<v-container>
  <h1 class="text-h6 my-4 d-flex align-center">
    Tasks
    <v-chip class="ml-2" density="comfortable">
      {{ tasks.length }}
    </v-chip>
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          class="ml-auto"
          color="secondary"
          prepend-icon="mdi-plus"
          text="Add"
          variant="flat"
          v-bind="activatorProps"
        ></v-btn>
      </template>

      <v-card title="Schedule task">
        <v-card-text>
          <v-row dense>
            <v-col cols="6">
              <v-select
                :items="['git']"
                label="Backend"
                hide-details
                required
              ></v-select>
            </v-col>

            <v-col cols="6">
              <v-select
                :items="['commits']"
                label="Category"
                hide-details
                required
              ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="URI"
                hide-details
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
          <v-col cols="6">
            <v-radio-group density="comfortable" size="small">
              <template v-slot:label>
                <span class="text-subtitle-2">Interval</span>
              </template>
              <v-radio :value="10080" label="Every week"></v-radio>
              <v-radio :value="43800" label="Every month"></v-radio>
              <v-radio value="custom" label="Custom"></v-radio>
            </v-radio-group>
            <v-text-field
              label="Every"
              type="number"
              suffix="minutes"
              class="ml-8"
              dense
              hide-details
              outlined
            >
            </v-text-field>
          </v-col>
        </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            text="Cancel"
            variant="plain"
            @click="dialog = false"
          ></v-btn>

          <v-btn
            color="primary"
            text="Save"
            variant="tonal"
            @click="dialog = false"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </h1>
  <task-list-item v-for="task in tasks"
    :backend="task.backend"
    :category="task.category"
    :status="task.status"
    :executions="task.executions"
    :id="task.id"
    :jobs="task.jobs"
    :scheduledDate="task.scheduledDate"
    :lastExecution="task.lastExecution"
    class="mb-3"
  ></task-list-item>
  <v-pagination
    :length="1"
    color="primary"
    density="comfortable"
  ></v-pagination>
</v-container>
</template>
<script>
import TaskListItem from './../stories/TaskListItem.vue';
export default {
  name: "TaskList",
  components: { TaskListItem },
  data() {
    return {
      dialog: false,
      tasks: [
        {
          backend: "git",
          category: "commits",
          status: "started",
          executions: 10,
          id: "abcd12345",
          scheduledDate: "2024-03-25",
          lastExecution: "2024-03-18",
          jobs: [
            { status: 'started' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'failed' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
          ]
        },
        {
          backend: "github",
          category: "commits",
          status: "finished",
          executions: 8,
          id: "cdfgh5678",
          scheduledDate: "2024-03-27",
          lastExecution: "2024-03-20",
          jobs: [
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
          ]
        },
        {
          backend: "github",
          category: "issues",
          status: "failed",
          executions: 19,
          id: "jklmn9876",
          scheduledDate: "2024-03-27",
          lastExecution: "2024-03-20",
          jobs: [
            { status: 'failed' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'failed' },
            { status: 'failed' },
            { status: 'failed' },
            { status: 'finished' },
            { status: 'finished' },
            { status: 'finished' },
          ]
        }
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
:deep(.v-radio-group) > .v-input__control > .v-label {
  margin-inline-start: 0;

  & + .v-selection-control-group {
    padding-inline-start: 0;
  }
}
</style>