import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/top-history-creators',
      name: 'top_history_creators',
      component: () => import('../views/TopHistoryCreators.vue')
    },
    {
      path: '/ads-message',
      name: 'ads_message',
      component: () => import('../views/AdsMessage.vue')
    },
    {
      path: '/top-ads-creators',
      name: 'top_ads_creators',
      component: () => import('../views/TopAdCreators.vue')
    },
    {
      path: '/minutes',
      name: 'minutes',
      component: () => import('../views/Minutes.vue')
    },
    {
      path: '/timeofday',
      name: 'timeofday',
      component: () => import('../views/TimeOfDay.vue')
    }
  ]
})

export default router