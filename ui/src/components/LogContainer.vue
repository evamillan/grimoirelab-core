<template>
  <code>
    <p v-for="log in logs" :key="log.created">
      {{ new Date(log.created * 1000).toLocaleString() }} [{{ log.module }}] {{ log.msg }}
    </p>
  </code>
</template>
<script>
export default {
  name: 'LogContainer',
  props: {
    logs: {
      type: Array,
      required: true
    }
  }
}
</script>
<style lang="scss" scoped>
code {
  display: block;
  background-color: rgb(var(--v-theme-on-surface));
  color: rgb(var(--v-theme-surface));
  padding: 1rem;
  border-radius: 4px;
  font-size: 0.8rem;
  white-space: pre-wrap;

  p {
    padding: 4px;
  }
}
</style>
