<template lang="html">
  <section>
    <sheet-item></sheet-item>
  </section>
</template>

<script>
import item from './item.vue'
export default {
  components:{
    'sheet-item':item,
  }
}
</script>

<style lang="scss" scoped>
  section{
    width: 100%;

    overflow-y: scroll;
    background: #fff;
  }
</style>
