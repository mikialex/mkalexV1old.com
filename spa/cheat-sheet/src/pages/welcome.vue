<template lang="html">
  <section>
    <p>Welcome to the constructing page of mkalex's cheet-sheet project</p>
    <p>Cheet-sheet is a notebook service for develops who use too many franeworks & librarys
      to remember theirs usage detail.To fulfill this demands,I make effort to develop an
      online notebook to help developers take useful notes on what they could quick&dirty
       use in their daily work.
    </p>
    <p>By the wonderful UI UX design and more advancing .
    I wish the whole notebook can be used ,written,and shared anytime anywhere with any user.</p>
    <p style="text-align:right">mk 2017 5 3</p>
    <router-link :to="{path:'/reading'}">take static view</router-link>
  </section>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
  section{
    padding-top: 100px;
    >p{
      margin:auto;
      margin-bottom: 20px;
      max-width: 500px;
      text-align: left;
      text-align: justify;
    }
  }
</style>
