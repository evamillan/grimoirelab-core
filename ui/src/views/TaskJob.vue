<template>
  <div class="mt-4">
    <v-card :class="'border-' + status" class="pa-2" variant="outlined">
      <v-card-title class="text-subtitle-2 pb-0">
          Job {{ $route.params.jobid }}
        <v-chip :color="status" class="ml-3" density="comfortable" size="small">
          {{ status }}
        </v-chip>
      </v-card-title>
      <div class="pl-4 mt-2">
        <p class="text-body-2 mb-2">
          Fetched
          <span class="font-weight-medium">
            {{ result.fetched }}
          </span>
        </p>
        <p class="text-body-2 mb-2">
          Skipped
          <span class="font-weight-medium">
            {{ result.skipped }}
          </span>
        </p>
      </div>
    </v-card>
    <div class="mt-4">
      <code v-for="log in logs">
        {{ log }}
      </code>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      status: "finished",
      result: {
        fetched: 250,
        skipped: 0,
      },
      logs: [
        'commit 456a68ee1407a77f3e804a30dff245bb6c6b872f ce8e0b86a1e9877f42fe9453ede418519115f367',
        '51a3b654f252210572297f47597b31527c475fb8 (HEAD -> refs/heads/master)',
        'Merge: ce8e0b8 51a3b65',
        'Author:     Zhongpeng Lin (林中鹏) <lin.zhp@example.com>',
        'AuthorDate: Tue Feb 11 22:10:39 2014 -0800',
        'Commit:     Zhongpeng Lin (林中鹏) <lin.zhp@example.com>',
        'CommitDate: Tue Feb 11 22:10:39 2014 -0800',
        ' ',
        `    Merge branch 'lzp'`,
        '    Conflicts:',
    	  '   	 aaa/otherthing',
        ' ',
        '1	0	aaa/otherthing.renamed',
        '::100644 100644 100644 e69de29... 58a6c75... 58a6c75... MR	aaa/otherthing.renamed'
      ]
    }
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