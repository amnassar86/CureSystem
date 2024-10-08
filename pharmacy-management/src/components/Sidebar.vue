<!-- src/components/Sidebar.vue -->
<template>
  <el-menu
    :default-active="activeMenu"
    class="el-menu-vertical-demo"
    background-color="#3A7CA5"
    text-color="#fff"
    active-text-color="#ffd04b"
    unique-opened
    router
  >
    <!-- لون أزرق مناسب للمجال الطبي -->
    <el-menu-item index="/dashboard">
      <i class="el-icon-menu"></i>
      <span>{{ $t('dashboard') }}</span>
    </el-menu-item>
    <el-submenu index="invoices">
      <template #title>
        <i class="el-icon-document"></i>
        <span>{{ $t('invoices') }}</span>
      </template>
      <el-menu-item index="/invoices">{{ $t('manage_invoices') }}</el-menu-item>
      <el-menu-item index="/invoices/archive">{{ $t('archive_invoices') }}</el-menu-item>
    </el-submenu>
    <el-menu-item index="/medicines">
      <i class="el-icon-medal"></i>
      <span>{{ $t('medicines') }}</span>
    </el-menu-item>
    <!-- إضافة عناصر القائمة الأخرى بنفس الطريقة -->
  </el-menu>
</template>

<script>
import { useRoute } from 'vue-router';
import { ref, watch } from 'vue';

export default {
  setup() {
    const route = useRoute();
    const activeMenu = ref(route.path);

    watch(
      () => route.path,
      (newPath) => {
        activeMenu.value = newPath;
      }
    );

    return {
      activeMenu,
    };
  },
};
</script>

<style scoped>
.el-menu-vertical-demo {
  height: 100%;
  border-right: none;
}
</style>
