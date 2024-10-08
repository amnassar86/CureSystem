// src/store/auth.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false);
  const user = ref(null);

  const login = (userData) => {
    isAuthenticated.value = true;
    user.value = userData;
    // تخزين الحالة في التخزين المحلي
    localStorage.setItem('auth', JSON.stringify({ isAuthenticated: true, user: userData }));
  };

  const logout = () => {
    isAuthenticated.value = false;
    user.value = null;
    // إزالة الحالة من التخزين المحلي
    localStorage.removeItem('auth');
  };

  // استعادة حالة المصادقة من التخزين المحلي عند تحميل التطبيق
  const initializeAuth = () => {
    const storedAuth = JSON.parse(localStorage.getItem('auth'));
    if (storedAuth && storedAuth.isAuthenticated) {
      isAuthenticated.value = storedAuth.isAuthenticated;
      user.value = storedAuth.user;
    }
  };

  return {
    isAuthenticated,
    user,
    login,
    logout,
    initializeAuth
  };
});
