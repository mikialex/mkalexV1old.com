<template lang="html">
  <nav>
    <nav-logo></nav-logo>
  </nav>
</template>

<script>
import logo from './cheet-sheet-nav-logo.vue'
export default {
  components:{
    'nav-logo':logo
  }
}
</script>

<style lang="scss" scoped>
@import "~globalSass";
nav{
  width:100%;height:r(20);
  position:fixed;top:0px;
  background: #000;
}
</style>
