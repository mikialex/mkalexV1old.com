<template lang="html">
  <section>
    <div class="" v-html="contentHtml">

    </div>
  </section>
</template>

<script>
import {markdown} from 'markdown';
export default {
  data(){
    return {
      content:'*loading*'
    }
  },
  computed:{
    contentHtml(){
      return markdown.toHTML(this.content)
    }
  },
  mounted(){
    // this.content=markdown.toHTML( "Hello *World*!" )
  }
}
</script>

<style lang="scss" scoped>
section{
  flex-grow: 1;
  height: 100vh;
  overflow-y: scroll;
}
</style>
