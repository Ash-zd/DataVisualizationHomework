<template>
  <div id="app">
    <dashboard/>
  </div>
</template>

<script>
import dashboard from '@/components/dashboard'
import myparallel from '@/components/parallel'

export default {
  name: 'App',
  components: {
    dashboard,
    myparallel
  },
  created () {}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  position: absolute;
  height: 100%;
  width: 100%;
}

</style>
