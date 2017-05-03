<template lang="html">
  <section>
    <project-slot></project-slot>
    <item-list></item-list>
    <page-detail></page-detail>
  </section>
</template>

<script>
import projectSlot from '@/components/project-slot/container.vue'
import itemList from '@/components/middle-panel/item-list.vue'
import pageDetail from '@/components/reading-page/page-detail.vue'
export default {
  components:{
    'project-slot':projectSlot,
    'item-list':itemList,
    'page-detail':pageDetail,
  }
}
</script>

<style lang="scss" scoped>
section{
display: flex;
}
</style>
