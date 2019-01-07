<style lang="stylus" scoped>
</style>


<template>
  <el-row type="flex" justify="center" align="middle" style="width: 100%; height: 100%; ">
    <el-card style="width: 30%; height: 60%" :body-style="{ height: '80%' }">
      <div slot="header" style="text-align: center">
        <span>登录</span>
      </div>
        <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm" class="form"  label-width="80px"
                 style="width: 90%; height: 80%; padding-top: 10%">
          <el-row type="flex" justify="center" >
            <el-form-item label="账号" prop="username">
              <el-input type="text" autocomplete="off" v-model="loginForm.username"></el-input>
            </el-form-item>
          </el-row>
          <el-row type="flex" justify="center" style="padding-top: 10%">
            <el-form-item label="密码" prop="password">
              <el-input type="password" autocomplete="off" v-model="loginForm.password"></el-input>
            </el-form-item>
          </el-row>
          <el-row type="flex" justify="center" style="padding-top: 10%">
            <el-form-item>
              <el-button type="primary" @click="submitForm('loginForm')" size="medium">提交</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="info" @click="resetForm('loginForm')" size="medium">重置</el-button>
            </el-form-item>
          </el-row>
        </el-form>
    </el-card>
  </el-row>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "login",
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
            axios.post('http://localhost:8000/api/admin/auth/', {
              username: this.loginForm.username,
              password: this.loginForm.password
            }).then((res) => {
              if (res.status === 200) {
                localStorage.setItem('token', res.data['token']);
                this.$store.commit("login");
                console.log(this.$store.state.isLogin);
                this.$router.push("dashboard")
              }
            }).catch(() => {
              this.$message.error('账号/密码错误')
            })
          } else {
            this.$message.error('格式错误');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>
