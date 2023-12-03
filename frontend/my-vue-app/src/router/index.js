import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/top-history-creators',
      name: 'top_history_creators',
      component: () => import('../views/TopHistoryCreators.vue')
    },
  ]
})

export default router