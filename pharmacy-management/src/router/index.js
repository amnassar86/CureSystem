// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '../layouts/MainLayout.vue';
import Login from '../pages/Login.vue';
import Dashboard from '../pages/Dashboard.vue';
import Invoices from '../pages/Invoices.vue';
import Medicines from '../pages/Medicines.vue';
import { useAuthStore } from '../store/auth';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: { requiresAuth: true }
      },
      {
        path: 'invoices',
        name: 'Invoices',
        component: Invoices,
        meta: { requiresAuth: true }
      },
      {
        path: 'medicines',
        name: 'Medicines',
        component: Medicines,
        meta: { requiresAuth: true }
      }
      // تعريف المسارات الأخرى كأطفال لـ MainLayout
    ]
  }
  // يمكنك إضافة مسارات إضافية هنا إذا لزم الأمر
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// حارس المسارات
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
