<template lang="html">
  <section>
    <project-icon></project-icon>
    <project-icon></project-icon>
    <project-icon></project-icon>
  </section>
</template>

<script>
import icon from './block.vue'
export default {
  components:{
    'project-icon':icon,
  }
}
</script>

<style lang="scss" scoped>
@import "~globalSass";
section{
  width:r(55);height:100vh;
  background: rgb(94, 94, 94);
  padding-top: 25px;
  display: flex;flex-direction: column;
  align-items: center;
}
</style>
