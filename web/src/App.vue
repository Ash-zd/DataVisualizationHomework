<style lang="stylus" rel="stylesheet/stylus">
  .page
    background-color #8391a5
    position absolute
    height 100%
    width 100%
.mainApp
  position absolute
  height 100%
  width 100%
  background-color #8391a5
</style>

<template>
  <div class="page">
    <el-container>
      <div class="page">
        <el-header>
          This is header.
        </el-header>
        <el-main>
          <div class="mainApp">
            <router-view></router-view>
          </div>
        </el-main>
      </div>
    </el-container>
  </div>
</template>

<script>

export default {
  data() {
    return {
      seller: {}
    }
  },
  created() {}
}

</script>
