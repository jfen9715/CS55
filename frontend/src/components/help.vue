<template>
  <section class="container">
    <section class="help_con">
      <h3>GET HELP</h3>
      <div class="help_para">{{title}}</div>
      <div class="help_para" v-for="(ctx, index) in context" :key="index">
        <p class="help_ctx">{{ctx.title}}</p>
        <p class="help_ctx" v-for="(item, idx) in ctx.items" :key="idx+100">
          <span class="strong">{{item.title}}</span> {{item.context}}
        </p>
      </div>
    </section>
  </section>
</template>

<script>
import { helpData } from '@/assets/js/data.js'
export default {
  data () {
    return {
      ...helpData
    }
  }
  // methods: {
  // }
}
</script>
<style scoped>
  .container {
    width: 100%;
    height: calc(100vh - 61px);
    padding-top: 61px;
    position: fixed;
    background: url('../assets/img/bg_login.jpg') no-repeat;
    background-size: 100%;
    background-position: center;
  }
  .help_con {
    width: auto;
    height: calc(100vh - 101px);
    font-size: 20px;
    background-color: rgba(0, 0, 0, .5);
    color: #ffffff;
    padding: 20px 60px;
    overflow: auto;
  }
  .help_para {
    margin: 20px 0;
  }
  .help_ctx {
    margin: 10px 0;
  }
  .strong {
    color: #e89c2c;
    font-weight: 600;
  }
  @media screen and (max-width: 977px) {
    .container {
      background-size: auto 100%;
    }
  }
  @media screen and (max-width: 800px) {
    .container {
      position: relative;
      background-size: auto 100%;
      overflow: auto;
    }
    .help_con {
      height: calc(100vh - 81px);
      padding: 10px 20px;
    }
  }
</style>
