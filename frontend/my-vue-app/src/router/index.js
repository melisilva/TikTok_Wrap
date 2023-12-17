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
      path: '/top-history-sounds',
      name: 'top_history_sounds',
      component: () => import('../views/TopHistorySounds.vue')
    },
    {
      path: '/top-hashtags',
      name: 'top_hashtags',
      component: () => import('../views/TopHashtags.vue')
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
    },
    {
      path: '/top-creator-overall',
      name: 'top_creator_overall',
      component: () => import('../views/TopCreator.vue')
    },
    {
      path: '/summary',
      name: 'summary',
      component: () => import('../views/Summary.vue')
    },
    {
      path: '/trends-message',
      name: 'trends_message',
      component: () => import('../views/TrendsMessage.vue')
    }
  ]
})

export default router