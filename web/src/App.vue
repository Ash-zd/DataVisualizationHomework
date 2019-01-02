<style lang="stylus" rel="stylesheet/stylus">
  .page
    background-color #545c64
    position absolute
    height 100%
    width 100%
    .header
      text-align center
    .mainApp
      position absolute
      height 88%
      width 98%
      background-color #545c64
</style>

<template>
  <div class="page">
    <div class="header">
      <el-menu
        class="el-menu-demo"
        router=true
        mode="horizontal"
        background-color="#344152"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-row type="flex" class="row-bg" justify="space-between">
          <el-col :span="24">
            <el-menu-item index="dashboard">资源监视器 v1.0</el-menu-item>
          </el-col>
          <el-col :span="24" offset="20" class="">
            <el-menu-item index="#">
              <el-dropdown trigger="click" class="el-dropdown-link" placement="bottom-start">
                <span style="color: #fff;">登录</span>
                <el-dropdown-menu slot="dropdown">
                  <el-form :label-position='left' label-width="60px">
                    <el-form-item label="账号:">
                      <el-input type="text" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="密码:">
                      <el-input type="password" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item>
                      <el-button type="primary">提交</el-button>
                      <el-button>重置</el-button>
                    </el-form-item>
                  </el-form>
                </el-dropdown-menu>
              </el-dropdown>
            </el-menu-item>
          </el-col>
        </el-row>
      </el-menu>
    </div>
    <div class="container">
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

export default {
  data () {
    return {
      seller: {}
    }
  },
  created () {}
}

</script>
