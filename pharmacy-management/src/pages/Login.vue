<!-- src/pages/Login.vue -->
<template>
  <div class="login-container">
    <h2>{{ $t('login') }}</h2>
    <el-form :model="loginForm" :rules="rules" ref="loginFormRef" label-width="120px" @submit.prevent="handleLogin">
      <el-form-item label="Username" prop="username">
        <el-input v-model="loginForm.username" placeholder="Enter username"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="loginForm.password" placeholder="Enter password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleLogin">{{ $t('login') }}</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../store/auth';
import { ElMessage } from 'element-plus';

export default {
  name: 'Login',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const loginForm = ref({
      username: '',
      password: ''
    });

    const loginFormRef = ref(null);

    const rules = {
      username: [
        { required: true, message: 'Please enter username', trigger: 'blur' }
      ],
      password: [
        { required: true, message: 'Please enter password', trigger: 'blur' }
      ]
    };

    const handleLogin = () => {
      loginFormRef.value.validate((valid) => {
        if (valid) {
          // تحقق من اسم المستخدم وكلمة المرور ثابتة
          const { username, password } = loginForm.value;
          if (username === 'admin' && password === 'password') {
            authStore.login({ username: 'admin' });
            router.push('/dashboard');
          } else {
            // عرض رسالة خطأ باستخدام Element Plus
            ElMessage.error('Invalid credentials');
          }
        } else {
          console.log('error submit!');
          return false;
        }
      });
    };

    return {
      loginForm,
      handleLogin,
      rules,
      loginFormRef
    };
  }
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
