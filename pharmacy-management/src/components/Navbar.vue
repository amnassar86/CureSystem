<!-- src/components/Navbar.vue -->
<template>
  <el-header class="navbar">
    <div class="navbar-content">
      <div class="logo-container">
        <img src="@/assets/logo.png" alt="Pharmacy Logo" class="logo-image" />
        <div class="logo-text">صيدلية</div>
      </div>
      <el-input
        placeholder="بحث..."
        prefix-icon="el-icon-search"
        class="search-box"
        v-model="searchQuery"
      ></el-input>
      <div class="navbar-right">
        <el-dropdown @command="handleLanguageChange">
          <span class="el-dropdown-link">
            {{ currentLanguage === 'ar' ? 'العربية' : 'English' }}
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="en">English</el-dropdown-item>
            <el-dropdown-item command="ar">العربية</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-badge :value="notificationCount" class="notification">
          <i class="el-icon-bell"></i>
        </el-badge>
        <el-dropdown>
          <span class="el-dropdown-link">
            <i class="el-icon-user"></i> المستخدم
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>{{ $t('profile') }}</el-dropdown-item>
            <el-dropdown-item @click="logout">{{ $t('logout') }}</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
  </el-header>
</template>

<script>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import { useAuthStore } from '../store/auth';

export default {
  setup() {
    const { locale } = useI18n();
    const currentLanguage = ref(locale.value);
    const notificationCount = ref(5); // مثال على عدد الإشعارات
    const searchQuery = ref('');
    const authStore = useAuthStore();

    const handleLanguageChange = (cmd) => {
      locale.value = cmd;
      currentLanguage.value = cmd;
      // تغيير الاتجاه حسب اللغة
      document.documentElement.dir = cmd === 'ar' ? 'rtl' : 'ltr';
    };

    const logout = () => {
      authStore.logout();
    };

    return {
      currentLanguage,
      notificationCount,
      searchQuery,
      handleLanguageChange,
      logout,
    };
  },
};
</script>

<style scoped>
.navbar {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}
.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}
.logo-container {
  display: flex;
  align-items: center;
}
.logo-image {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}
.logo-text {
  font-size: 24px;
  font-weight: bold;
  color: #3A7CA5; /* لون أزرق يعبر عن المجال الطبي */
}
.search-box {
  width: 300px;
}
.navbar-right {
  display: flex;
  align-items: center;
}
.notification {
  margin-right: 20px;
}
</style>
