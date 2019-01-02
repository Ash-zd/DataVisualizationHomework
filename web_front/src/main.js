// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import cpu from '@/components/cpu'
import memory from '@/components/memory'
import disk from '@/components/disk'
import net from '@/components/net'
import dashboard from '@/components/dashboard'
import VueRouter from 'vue-router'
import parallel from '@/components/parallel'
import tree from '@/components/tree'

Vue.use(VueRouter)
Vue.use(ElementUI)

Vue.config.productionTip = false

const router = new VueRouter({
  routes: [{
    path: '/dashboard',
    component: dashboard
  }, {
    path: '/cpu',
    component: cpu
  }, {
    path: '/memory',
    component: memory
  }, {
    path: '/disk',
    component: disk
  }, {
    path: '/net',
    component: net
  }, {
    path: '/parallel',
    component: parallel
  }, {
    path: '/tree',
    component: tree
  }],
  linkActiveClass: 'active'
})

new Vue({
  router,
  template: '<App>',
  components: {
    App
  },
  data: {
    eventHub: new Vue(),
    charts: []
  }
}).$mount('#app')
