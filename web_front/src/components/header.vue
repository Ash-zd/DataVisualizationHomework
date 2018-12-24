<template>
<div class="header">
  <h1 class="el-icon-info"> 资源监视器 v1.0</h1>
  <hr>
</div>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
.header{
  text-align: center;
}
</style>
