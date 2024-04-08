<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Breadcrumbs from './components/Breadcrumbs.vue'
</script>

<template>
  <v-app>
    <v-app-bar color="primary" density="compact" flat>
      <template v-slot:prepend>
        <img src="./assets/favicon.png" height="30">
      </template>
    </v-app-bar>
    <v-navigation-drawer
      class="pa-2"
      color="transparent"
      permanent
    >
      <v-list color="primary" density="compact">
        <v-list-item to="/">
          <template v-slot:prepend>
            <v-icon>mdi-home-outline</v-icon>
          </template>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item>
        <v-list-item :to="{name: 'taskList'}">
          <template v-slot:prepend>
            <v-icon>mdi-calendar</v-icon>
          </template>
          <v-list-item-title>Tasks</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <Breadcrumbs />
      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped lang="scss">
:deep(.v-toolbar__prepend) {
  margin-inline: 14px auto;
}
.v-navigation-drawer {
  .v-list-item.v-list-item--density-compact {
    border-radius: 4px;
    padding-inline: 8px;

    :deep(.v-list-item__spacer) {
      width: 16px;
    }
  }
  .v-list-item-title {
    font-size: 0.875rem;
    font-weight: 500;
    line-height: 1.375rem;
    letter-spacing: 0.0071428571em;
  }
}
</style>
