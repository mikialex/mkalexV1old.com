<template lang="html">
  <section>
    <main class="" >
      <slot></slot>
    </main>
  </section>
</template>

<script>
export default {

  mounted(){
    // this.content=markdown.toHTML( "Hello *World*!" )
  }
}
</script>

<style lang="scss" scoped>
section{
  flex-grow: 1;
  background: url(../../assets/sand-back.png);
  background-size: 40px 40px;
  overflow-y: scroll;
  display: flex;flex-direction: column;
  align-items: center;
  padding: 30px;
  >main{
    width: 100%;
    margin:30px;
    background: #fff;
    box-shadow: 0 2px 39px 0 rgba(0,0,0,0.09), 0 2px 4px 0 rgba(0,0,0,0.19);
    border-radius: 2px;
  }
}
</style>
