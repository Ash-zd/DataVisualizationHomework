<style lang="stylus" rel="stylesheet/stylus">
  .page
    background-color #003264
    position absolute
    height 100%
    width 100%
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    .header
      text-align center
    .mainApp
      position absolute
      height 97%
      width 97%
  .content
    // background-color #545c64
    background-color #003964
    position absolute
    height 100%
    width 100%
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
</style>

<template>
  <div class="page">
    <div class="header">
      <v-header></v-header>
    </div>
    <div class="content">
      <el-container>
        <el-main>
          <div class="mainApp">
            <router-view></router-view>
          </div>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
import header from 'src/components/page/header'

export default {
  data () {
    return {
      seller: {}
    }
  },
  created () {},
  components: {
    'v-header': header
  }
}

</script>
