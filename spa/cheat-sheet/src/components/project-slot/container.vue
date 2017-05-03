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
  width:r(55);
  // height: 100vh;
  height:100%;
  background-image:url(../../assets/project-slot-container-back.png);
  background-size: 25px 25px;
  display: flex;flex-direction: column;
  align-items: center;
  box-shadow: inset 0px 5px 5px 0px rgba(0, 0, 0, 0.2);
}
</style>
