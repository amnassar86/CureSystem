<!-- src/layouts/MainLayout.vue -->
<template>
  <el-container style="height: 100vh">
    <el-header class="header-shadow">
      <Navbar />
    </el-header>
    <el-container>
      <el-aside width="200px" class="sidebar-shadow">
        <Sidebar />
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Sidebar from '../components/Sidebar.vue';

export default {
  components: {
    Navbar,
    Sidebar,
  },
};
</script>

<style scoped>
.header-shadow {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}
.sidebar-shadow {
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
}
</style>
