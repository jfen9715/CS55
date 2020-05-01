<template>
  <section class="login_container">
    <section v-if="!isLogin" class="login_con">
      <section class="login_tip">
        <p v-for="(item,index) in loginData" :key="index">{{item}}</p>
      </section>
      <section class="login_main">
        <el-tabs v-model="currentItem">
          <el-tab-pane name="signup" label="Sign up">
            <el-form label-position="top" :model="signForm" label-width="100px">
              <el-form-item label="Email Address">
                <el-input v-model="signForm.email" size="small"></el-input>
              </el-form-item>
              <el-form-item label="Username">
                <el-input v-model="signForm.username" size="small"></el-input>
              </el-form-item>
              <el-form-item label="Password">
                <el-input v-model="signForm.password" type="password" size="small"></el-input>
              </el-form-item>
              <el-form-item label="Confirm Password">
                <el-input v-model="signForm.cpassword" type="password" size="small"></el-input>
              </el-form-item>
              <el-form-item>
                <el-checkbox v-model="anonymous" label="submit anonymously"></el-checkbox>
              </el-form-item>
              <el-form-item>
                <el-button v-if="!anonymous" type="primary" @click="toSignUp">Sign up</el-button>
                <el-button v-else type="primary" @click="toAnonymously">Login anonymously</el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>
          <el-tab-pane name="login" label="Login">
            <el-form label-position="top" :model="userForm" label-width="100px">
              <el-form-item label="Email">
                <el-input v-model="userForm.email" size="small"></el-input>
              </el-form-item>
              <el-form-item label="Password">
                <el-input v-model="userForm.password" type="password" size="small"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="toLogin">Login</el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>
        </el-tabs>
      </section>
    </section>
    <section v-else class="user_con">
      <p>Welcome {{isAnonymous ? email : userName}}!</p>
      <section class="user_btn">
        <el-button v-if="finished" class="user_btn_s" type="primary" @click="toStart">Start Now</el-button>
        <template v-else>
          <el-button class="user_btn_s" type="primary" @click="toStart">Restart</el-button>
          <el-button class="user_btn_s" type="primary" @click="toStart">Continue</el-button>
        </template>
      </section>
    </section>
  </section>
</template>
<script>

import { loginData } from '@/assets/js/data.js'
export default {
  data () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please input confirm password.'))
      } else if (value !== this.userForm.password) {
        callback(new Error('Password and confirm password do not match!'))
      } else {
        callback()
      }
    }
    return {
      isLogin: false,
      loginData,
      userName: '',
      email: '',
      isAnonymous: false,
      finished: true,
      signForm: {
        email: '',
        username: '',
        password: '',
        cpassword: ''
      },
      userForm: {
        email: '',
        password: ''
      },
      currentItem: 'signup',
      anonymous: false
    }
  },
  methods: {
    toLogin () {
      let _this = this
      let data = new URLSearchParams()
      data.append('user_password', this.userForm.password)
      data.append('user_email', this.userForm.email)
      this.$axios.post('/login/verify/', data)
        .then(function (response) {
          if (response.data.status === 0) {
            _this.userName = _this.userForm.email
            sessionStorage.setItem('user_email', _this.userForm.email)
            _this.finished = response.data.finished
            _this.isLogin = true
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    toSignUp () {
      let _this = this
      let data = new URLSearchParams()
      data.append('user_name', this.signForm.username)
      data.append('user_password', this.signForm.password)
      data.append('user_email', this.signForm.email)
      this.$axios.post('/login/register/', data)
        .then(function (response) {
          if (response.data.status === 0) {
            _this.userName = _this.signForm.email
            sessionStorage.setItem('user_email', _this.signForm.email)
            _this.isLogin = true
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    toAnonymously () {
      this.isAnonymous = true
      sessionStorage.setItem('user_email', 'Anonymous')
    },
    toStart () {
      if (this.finished === true) {
        sessionStorage.setItem('continue', 'false')
        this.$router.push('/modules')
      } else {
        let data = new URLSearchParams()
        data.append('user_email', sessionStorage.getItem('user_email'))
        this.$axios.post('/login/data/', data)
          .then(function (response) {
            console.log(response.data)
            // Load data in sessionStorage
          })
        sessionStorage.setItem('continue', 'true')
        this.$router.push('/modules')
      }
    }
  }
}
</script>
<style scoped>
  .login_container {
    width: 100%;
    min-height: calc(100vh - 61px);
    padding-top: 61px;
    /* position: fixed; */
    background: url('../assets/img/bg_login.jpg') no-repeat;
    background-size: 100%;
    background-position: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    align-content: center;
    justify-content: center;
  }
  .login_con {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
  }
  .login_tip {
    width: 30%;
    height: 500px;
    overflow: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #111417;
    background-color: rgba(255, 255, 255, .4);
    margin: 0 2% 0 25%;
  }
  .login_tip p {
    font-size: 20px;
    margin: 10px 20px;
  }
  .login_main {
    width: 350px;
    height: 500px;
    justify-content: center;
    background-color: rgba(255, 255, 255, .4);
  }
  .el-tabs {
    width: 100%;
    height: 100%;
  }
  .el-tabs /deep/ .el-tabs__nav {
    width: 100%;
  }
  .el-tabs /deep/ .el-tabs__item {
    width: 50%;
    font-size: 18px;
    text-align: center;
  }
  .el-tab-pane {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .el-form{
    height: auto;
  }
  .el-tab-pane:first-child .el-form /deep/ .el-form-item {
    margin-bottom: 0;
  }
  .el-form-item /deep/ .el-input__inner {
    width: 240px;
  }
  .el-form /deep/ .el-form-item__label, .el-form /deep/ .el-checkbox__label {
    font-size: 20px;
    color: #111417;
    font-weight: 500;
    padding-bottom: 0;
  }
  .el-form /deep/ .el-button {
    font-size: 20px;
  }

  .user_con {
    width: 500px;
    height: 350px;
    background-color: rgba(255, 255, 255, .4);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
  }
  .user_con p {
    font-size: 22px;
    color: #111417;
    margin: 50px 0;
    text-align: center;
    line-height: 40px;
  }

  .user_btn {
    width: 100%;
    display: flex;
    margin-bottom: 30px;
    flex-direction: row;
    align-items: center;
    justify-content:center;
  }
  .user_btn_s {
    margin: 10px;
    font-size: 20px;
  }

  @media screen and (max-width: 800px) {
    .login_container {
      background-size: auto 100%;
    }
    .login_con {
      width: 100%;
      height: auto;
      display: block;
      background-color: rgba(255, 255, 255, .4);
    }
    .login_tip {
      width: 100%;
      margin-bottom: 20px;
      background: none;
      margin: 0;
    }
    .login_main, .user_con {
      width: 100%;
      height: auto;
      display: flex;
      align-items: center;
      align-content: center;
      justify-content: center;
      background: none;
    }
    .user_con {
      height: 350px;
      align-content: space-around;
    }
    .el-tabs {
      height: 450px;
    }
  }
</style>

