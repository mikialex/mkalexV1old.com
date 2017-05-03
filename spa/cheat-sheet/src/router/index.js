import Vue from 'vue'
import Router from 'vue-router'
import welcome from '@/pages/welcome.vue'
import reading from '@/pages/reading.vue'
import defaultSheet from '@/components/reading-page/default-sheet.vue'
import sheet from '@/components/reading-page/common-sheet.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name:'welcome',
      component:welcome
    }, {
      path: '/reading',
    //   name: 'reading',
      component: reading,
      children: [
          {
              path:'/',
              component:defaultSheet
          },
          {
              path: 'sheet',
              component: sheet
          },
      ]
  },
  ]
})
