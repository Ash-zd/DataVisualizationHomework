<template>
<div class="dashboard">
  <el-container>
    <el-aside width="200px">
      <navMenu/>
    </el-aside>
    <el-container>
      <el-header>
        <myHeader/>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</div>
</template>

<script>
import myHeader from '@/components/header'
import navMenu from '@/components/navMenu'
import cpu from '@/components/cpu'
import tree from '@/components/tree'
export default {
  name: 'dashboard',
  components: {
    cpu,
    myHeader,
    navMenu,
    tree
  }
}
</script>

<style scoped>
  .dashboard {
    position: relative;
    width: 100%;
    height: 100%;
    margin: 0px;
  }
</style>
