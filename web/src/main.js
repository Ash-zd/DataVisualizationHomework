import Vue from 'vue'
import App from './App'
import 'element-ui/lib/theme-chalk/index.css'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import column from 'components/column/column'
import heat from 'components/heat/heat'
import point from 'components/point/point'
import line from 'components/line/line'
import dashboard from 'components/dashboard/dashboard'
import multipleColumn from 'components/multipleColumn/multipleColumn'
import tree from 'components/tree/tree'
import login from 'components/login/login'

import ElementUI from 'element-ui'
import parallel from './components/parallel/parallel'

Vue.use(ElementUI)

Vue.use(VueRouter)
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0,
    color: ['#325B69', '#698570', '#AE5548', '#6D9EA8', '#9CC2B0', '#C98769'],
    baseUrl: "http://localhost:8000/api/"
  }
})
const router = new VueRouter({
  routes: [{
    path: '/column',
    component: column
  }, {
    path: '/heat',
    component: heat
  }, {
    path: '/point',
    component: point
  }, {
    path: '/dashboard',
    component: dashboard
  }, {
    path: '/multipleColumn',
    component: multipleColumn
  }, {
    path: '/line',
    component: line
  }, {
    path: '/parallel',
    component: parallel
  }, {
    path: '/tree',
    component: tree
  }, {
    path: '/login',
    component: login
  }],
  linkActiveClass: 'active'
})
new Vue({
  router,
  store,
  template: '<App>',
  components: {
    App
  },
  data: {
    eventHub: new Vue(),
    charts: []
  }
}).$mount('#app')

router.push('dashboard')
