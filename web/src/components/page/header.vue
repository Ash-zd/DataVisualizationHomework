<style scoped>

</style>

<template>
  <el-menu
    router=true
    mode="horizontal"
    background-color="#003964"
    text-color="#fff"
    active-text-color="#fff">
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-row type="flex" justify="start">
        <el-menu-item index="#" @click="goToDashboard">资源监视器 v1.0</el-menu-item>
      </el-row>
      <el-row type="flex" justify="center">
        <el-menu-item index="#" @click="getBattery">获取电量信息</el-menu-item>
      </el-row>
      <el-row type="flex" justify="end">
        <el-menu-item index="#" @click="goToLogin">登录</el-menu-item>
      </el-row>
    </el-row>
  </el-menu>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pageHeader',
  data() {
    let checkUsername = (rule, value, callback) => {
      if (!value || value === '') {
        return callback(new Error('账号不能为空'));
      }
      return callback();
    };
    let validatePass = (rule, value, callback) => {
      if (!value || value === '') {
        return callback(new Error('密码不能为空'));
      }
      return callback();
    };
    return {
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, validator: checkUsername, trigger: 'blur' }
        ],
        password: [
          { required: true, validator: validatePass, trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    getBattery() {
      axios.get(this.$store.state.baseUrl + '/api/battery/info/').then((res) => {
        this.$message({
          message: '剩余电量：' + res.data['percent'] + '%',
          type: 'success'
        })
      })
    },
    goToDashboard() {
      this.$router.push("dashboard");
    },
    goToLogin() {
      this.$router.push("login");
    }
  }
}
</script>
