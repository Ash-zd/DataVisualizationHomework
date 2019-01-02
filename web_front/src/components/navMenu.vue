<template>
  <div class="navMenu">
    <h3>导航</h3>
    <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <router-link to="/cpu">
        <el-menu-item index="1">
          <i class="el-icon-location"></i>
          <span>CPU</span>
        </el-menu-item>
      </router-link>
      <router-link to="/memory">
        <el-menu-item index="2">
          <i class="el-icon-tickets"></i>
          <span slot="title">内存</span>
        </el-menu-item>
      </router-link>
      <router-link to="/disk">
        <el-menu-item index="3">
          <i class="el-icon-document"></i>
          <span slot="title">硬盘</span>
        </el-menu-item>
      </router-link>
      <router-link to="/net">
        <el-menu-item index="4">
          <i class="el-icon-sort"></i>
          <span slot="title">网络</span>
        </el-menu-item>
      </router-link>
      <router-link to="/parallel">
        <el-menu-item index="5">
          <i class="el-icon-sort"></i>
          <span slot="title">parallel</span>
        </el-menu-item>
      </router-link>
      <router-link to="/tree">
        <el-menu-item index="5">
          <i class="el-icon-sort"></i>
          <span slot="title">tree</span>
        </el-menu-item>
      </router-link>
    </el-menu>
  </div>
</template>

<script>
export default {
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

h3 {
  text-align: center;
}
</style>
