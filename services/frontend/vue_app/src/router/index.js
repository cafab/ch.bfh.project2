import Vue from 'vue'
import Router from 'vue-router'
import { authGuard } from "../auth/authGuard";

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      beforeEnter: authGuard,
      component: () => import('@/views/Dashboard.vue')
    }
  ]
})
