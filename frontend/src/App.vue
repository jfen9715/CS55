<template>
  <div id="app">
    <header>
      <el-menu
        :default-active="currentItem"
        :router="true"
        class="el-menu-demo"
        mode="horizontal"
        menu-trigger="hover"
        background-color="#323f4f"
        text-color="#fff"
        active-text-color="#e89c2c">
        <el-menu-item index="/">Ready</el-menu-item>
        <el-menu-item index= "/modules">Modules</el-menu-item>
        <el-menu-item index= "/help" class="help">Need Help?</el-menu-item>
      </el-menu>
    </header>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  watch: {
    $route (to, from) {
      console.log('route, to', to, 'from', from)
      if (to.name === 'Modules') {
        this.currentItem = '/modules'
      } else if (to.name === 'Help') {
        this.currentItem = '/help'
      } else {
        this.currentItem = '/'
      }
    }
  },
  data () {
    return {
      currentItem: '/'
    }
  }
}
</script>

<style>
  body{
    margin: 0;
    padding: 0;
  }
  #app {
    width: 100vw;
    height: 100vh;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  header {
    position: fixed;
    width: 100%;
    padding: 0;
    z-index: 99;
  }
  .el-menu /deep/ .el-menu-item {
    font-size: 28px;
  }
  .el-menu /deep/ .el-menu-item:last-child {
    float: right;
  }
  @media screen and (max-width: 800px) {
    .el-menu /deep/ .el-menu-item {
      font-size: 20px;
      padding: 0 10px;
    }
  }
</style>
