<template lang="html">
  <section>
    <panel-header></panel-header>
    <item-list></item-list>
  </section>
</template>

<script>
import list from './item-list.vue'
import header from './header.vue'
export default {
  components:{
    'panel-header':header,
    'item-list':list,
  }
}
</script>

<style lang="scss" scoped>
section{
  width: 250px;
  height: 100%;
}
</style>
