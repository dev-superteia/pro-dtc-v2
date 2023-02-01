import { createRouter, createWebHistory } from 'vue-router'
import BaseLayout from '@/layout/BaseLayout.vue'
const routes = [
  {
    path: '/',
    component: BaseLayout,
    redirect: 'product_one_level',
    meta: {
      authRequired: true,
      hidden: true,
    },
    children: [    
      { 
        path: '/permission',
        name: 'permission', 
        component: () => import('@/views/user/permissions/index.vue'),
        meta: { transition: 'slide-right' },
       },
       { 
         path: '/roles',
         name: 'roles', 
        component: () => import('../views/user/roles/index.vue'),
         meta: { transition: 'slide-right' },
        },
        { 
          path: '/raw_material_and_compound',
          name: 'raw_material_and_compound', 
          component: () => import('../views/raw_material_and_compound/index.vue'),
          meta: { transition: 'slide-right' },
         },
        { 
          path: '/raw_material_without_cost',
          name: 'raw_material_without_cost', 
          component: () => import('../views/raw_material_without_cost/index.vue'),
          meta: { transition: 'slide-right' },
         },
        { 
          path: '/tissue_month',
          name: 'tissue_month', 
          component: () => import('../views/tissue_month/index.vue'),
          meta: { transition: 'slide-right' },
         },
        { 
          path: '/compound_and_fabric',
          name: 'compound_and_fabric', 
          component: () => import('../views/compound_and_fabric/index.vue'),
          meta: { transition: 'slide-right' },
         },
        { 
          path: '/product_raw_material',
          name: 'product_raw_material', 
          component: () => import('../views/product_raw_material/index.vue'),
          meta: { transition: 'slide-right' },
         },
        { 
          path: '/product_one_level',
          name: 'product_one_level', 
          component: () => import('../views/product_one_level/index.vue'),
          meta: { transition: 'slide-right' },
         },
    ],
  },
  { 
    path: '/login',
    name: 'dashboard4', 
    component: () => import('../views/auth/Login2.vue'),
    meta: { transition: 'slide-right' },
   },  

]

const router = createRouter({
        history: createWebHistory(),
        routes
      })
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record)) {
    next()
  } else {
    console.log('Not auth required')
    next()
  }
});

export default router