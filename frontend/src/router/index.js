import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: () => import('@/components/index')
    },
    {
      path: '/modules',
      name: 'Modules',
      component: () => import('@/components/modules')
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/components/login')
    },
    {
      path: '/help',
      name: 'Help',
      component: () => import('@/components/help')
    }
  ]
})
