<!-- src/pages/Medicines.vue -->
<template>
  <div class="medicines">
    <h1>{{ $t('medicines') }}</h1>
    <el-table :data="medicines" style="width: 100%" stripe>
      <el-table-column prop="id" label="ID" width="50" />
      <el-table-column prop="name" label="Name" />
      <el-table-column prop="category" label="Category" />
      <el-table-column prop="price" label="Price" />
      <el-table-column label="Actions" width="150">
        <template #default="scope">
          <el-button size="mini" type="primary" @click="editMedicine(scope.row)">
            {{ $t('edit') }}
          </el-button>
          <el-button size="mini" type="danger" @click="deleteMedicine(scope.row.id)">
            {{ $t('delete') }}
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" @click="addMedicine" style="margin-top: 20px;">
      {{ $t('add_medicine') }}
    </el-button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

export default {
  name: 'Medicines',
  setup() {
    const medicines = ref([
      { id: 1, name: 'Medicine A', category: 'Category 1', price: '$10' },
      { id: 2, name: 'Medicine B', category: 'Category 2', price: '$20' }
      // بيانات مؤقتة أخرى
    ]);

    const editMedicine = (medicine) => {
      // تعديل الدواء مؤقتًا
      ElMessage.info(`Editing Medicine ID: ${medicine.id}`);
    };

    const deleteMedicine = (id) => {
      // حذف الدواء مؤقتًا
      medicines.value = medicines.value.filter(medicine => medicine.id !== id);
      ElMessage.success('Medicine deleted successfully');
    };

    const addMedicine = () => {
      // إضافة دواء جديد مؤقتًا
      const newMedicine = {
        id: medicines.value.length + 1,
        name: `Medicine ${String.fromCharCode(64 + medicines.value.length + 1)}`,
        category: `Category ${medicines.value.length + 1}`,
        price: `$${10 * (medicines.value.length + 1)}`
      };
      medicines.value.push(newMedicine);
      ElMessage.success('Medicine added successfully');
    };

    return {
      medicines,
      editMedicine,
      deleteMedicine,
      addMedicine
    };
  }
};
</script>

<style scoped>
.medicines {
  padding: 20px;
}
</style>
