<!-- src/App.vue -->
<template>
  <div :dir="currentDirection">
    <router-view />
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n';
import { computed } from 'vue';

export default {
  setup() {
    const { locale } = useI18n();
    const currentDirection = computed(() => (locale.value === 'ar' ? 'rtl' : 'ltr'));

    return {
      currentDirection,
    };
  },
};
</script>

<style>
/* يمكنك إضافة أنماط إضافية هنا إذا لزم الأمر */
</style>
