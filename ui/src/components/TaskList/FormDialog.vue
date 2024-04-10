<template>
  <v-dialog v-model="isOpen" max-width="600">
    <template #activator="{ props: activatorProps }">
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
              v-model="formData.backend"
              :items="['git']"
              color="primary"
              label="Backend"
              hide-details
              required
            />
          </v-col>
          <v-col cols="6">
            <v-select
              v-model="formData.category"
              :items="['commit']"
              color="primary"
              label="Category"
              hide-details
              required
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="formData.backendArgs.uri"
              color="primary"
              label="URI"
              hide-details
              required
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="formData.backendArgs.gitpath"
              color="primary"
              label="Path"
              hide-details
              required
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-radio-group
              v-model="formData.schedulerArgs.interval"
              density="comfortable"
              size="small"
            >
              <template #label>
                <span class="text-subtitle-2">Interval</span>
              </template>
              <v-radio :value="86400" label="Every day"></v-radio>
              <v-radio :value="604800" label="Every week"></v-radio>
            </v-radio-group>
          </v-col>
        </v-row>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text="Cancel" variant="plain" @click="isOpen = false"></v-btn>
        <v-btn color="primary" text="Save" variant="flat" @click="onSave"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: 'FormDialog',
  emits: ['create'],
  data() {
    return {
      isOpen: false,
      formData: {
        backend: 'git',
        category: 'commit',
        backendArgs: {
          uri: '',
          gitpath: ''
        },
        schedulerArgs: {
          interval: 604800,
          max_retries: 1
        }
      }
    }
  },
  methods: {
    onSave() {
      this.$emit('create', this.formData)
      this.isOpen = false
    }
  }
}
</script>
