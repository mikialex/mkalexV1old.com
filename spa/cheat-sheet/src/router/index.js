import Vue from 'vue'
import Router from 'vue-router'
import reading from '@/pages/reading.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/reading'
    }, {
      path: '/reading',
      name: 'reading',
      component: reading
    }
  ]
})
