<template>
  <v-breadcrumbs :items="breadcrumbs"></v-breadcrumbs>
</template>
<script>
export default {
  name: "Breadcrumbs",
  computed: {
    breadcrumbs() {
      return this.$route.matched.filter(match => match.meta.breadcrumb)
                                 .map(route => {
                                  return {
                                    title: this.getTitle(route),
                                    to: route.meta.breadcrumb.to || { name: route.name },
                                    exact: true
                                  }
                                })
    }
  },
  methods: {
    getTitle(route) {
      if (route.meta.breadcrumb.param) {
        return `${route.meta.breadcrumb.title} ${this.$route.params[route.meta.breadcrumb.param]}`;
      } else {
        return route.meta.breadcrumb.title;
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.v-breadcrumbs {
  height: 68px;
}
</style>