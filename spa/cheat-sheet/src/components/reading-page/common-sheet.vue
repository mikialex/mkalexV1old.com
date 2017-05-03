<template lang="html">
  <div class="">
    common sheet
    <div class="" v-html="contentHtml">

    </div>
  </div>
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
}
</script>

<style lang="css">
</style>
