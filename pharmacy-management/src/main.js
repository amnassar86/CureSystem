// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import '@fortawesome/fontawesome-free/css/all.css';
import './styles/main.css';

import { createI18n } from 'vue-i18n';
import en from './locales/en.json';
import ar from './locales/ar.json';
import { useAuthStore } from './store/auth';

const i18n = createI18n({
  locale: 'ar', // اللغة الافتراضية
  fallbackLocale: 'en',
  messages: {
    en,
    ar,
  },
});

const pinia = createPinia();
const app = createApp(App);

app.use(router);
app.use(pinia);
app.use(ElementPlus);
app.use(i18n);

app.mount('#app');

// استعادة حالة المصادقة
const authStore = useAuthStore();
authStore.initializeAuth();
