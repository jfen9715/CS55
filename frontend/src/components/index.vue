<template>
  <section class="container">
    <section class="home">
      <section class="home_title">
        <section class="home_title_p">
          <p>{{title}}</p>
          <section class="home_title_pc">
            <p>Get Start</p>
            <p><i class="el-icon-bottom"></i></p>
          </section>
        </section>
      </section>
      <section class="home_main">
        <section class="card" v-for="(item, index) in context" :key="index">
          <p>{{item}}</p>
        </section>
      </section>
      <section class="btn">
        <el-button type="primary" @click="toStart">Start Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      </section>
    </section>
  </section>
</template>

<script>
import { indexData } from '@/assets/js/data.js'
import Modules from './modules.vue'
const titleBg = require('../assets/img/bg_title.jpg')
export default {
  components: {
    Modules
  },
  data () {
    return {
      ...indexData,
      titleBg: titleBg
    }
  },
  mounted () {

  },
  methods: {
    toStart () {
      this.$router.push('/login')
    }
  }
}
</script>
<style scoped>
  .container{
    width: 100%;
    padding-top: 61px;
    font-family: "Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
  .home, .module{
    width: 100%;
    position: relative;
    text-align: center;
  }
  .home_title {
    width: 100%;
    height: calc(100vh - 61px);
    background: url('../assets/img/bg_title.jpg') no-repeat;
    background-size: 100%;
    background-position-y: bottom;
  }
  .home_title_p {
    position: relative;
    width: 100%;
    height: 100%;
    background-color :rgba(0,0,0,0.55);
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    align-content: space-between;
    font-size: 60px;
    text-align: center;
    color: rgba(255,255,255,0.9);
  }
  .home_title_p p {
    margin: 10px auto;
  }
  .home_title_pc {
    position: absolute;
    bottom: 10px;
    color: #e89c2c;
  }
  .home_main {
    width: 100%;
    font-size: 20px;
    text-align: left;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    align-content: center;
  }
  .home_main p{
    margin: 20px 40px;
  }
  .card {
    display: flex;
    width: 400px;
    height: 300px;
    color: #323f4f;
    background-color: #fff;
    align-items: center;
  }
  .card:nth-child(1) p {
    margin: 20px;
  }
  .card:nth-child(2) {
    color: #fff;
    background-color: #e89c2c;
  }
  .home_img {
    width: 100%;
    height: auto;
  }
  .btn {
    position: absolute;
    right: 40px;
    bottom: 10px;
    text-align: right;
  }
  .btn .el-button{
    height: 50px;
    width: auto;
    font-size: 20px;
  }

  @media screen and (max-width: 800px) {
    .home {
      padding-bottom: 40px;
    }
    .home_title {
      display: inline-block;
      width: 90%;
      height: 200px;
      margin: 10px auto;
    }
    .home_title_p {
      font-size: 20px;
    }
    .home_title_pc{
      display: none;
    }
    .home_main {
      font-size: 20px;
      flex-direction: column;
    }
    .home_main p {
      margin: 20px;
    }
    .card {
      width: 90%;
      height: auto;

    }
    .btn {
      position: relative;
      width: 100%;
      margin: 10px 0;
    }
    .btn .el-button{
      margin-right: 20px;
      width: auto;
      font-size: 20px;
    }
  }
</style>
