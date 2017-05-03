<template lang="html">
  <section>
    <main>
      <project-slot></project-slot>
      <middle-panel></middle-panel>
      <page-detail>
        <router-view></router-view>
      </page-detail>
    </main>
  </section>
</template>

<script>
import projectSlot from '@/components/project-slot/container.vue'
import panel from '@/components/middle-panel/panel-all.vue'
import pageDetail from '@/components/reading-page/page-detail.vue'
export default {
  components:{
    'project-slot':projectSlot,
    'middle-panel':panel,
    'page-detail':pageDetail,
  }
}
</script>

<style lang="scss" scoped>
section{
  display: flex;
  flex-direction: column;
  height: 100%;
  >main{
    width:100%;
    margin-top: 20px;
    height: calc(100vh - 20px);
    // flex-grow: 1;
    display: flex;
    align-items: center;;
  }
}
</style>
