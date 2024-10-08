<!-- src/pages/Invoices.vue -->
<template>
  <div class="invoices">
    <h1>{{ $t('invoices') }}</h1>
    <el-table :data="invoices" style="width: 100%" stripe>
      <el-table-column prop="id" label="ID" width="50" />
      <el-table-column prop="date" label="Date" width="180" />
      <el-table-column prop="customer" label="Customer" />
      <el-table-column prop="total" label="Total" />
      <el-table-column label="Actions" width="150">
        <template #default="scope">
          <el-button size="mini" type="primary" @click="viewInvoice(scope.row)">
            {{ $t('view') }}
          </el-button>
          <el-button size="mini" type="danger" @click="deleteInvoice(scope.row.id)">
            {{ $t('delete') }}
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" @click="addInvoice" style="margin-top: 20px;">
      {{ $t('add_invoice') }}
    </el-button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

export default {
  name: 'Invoices',
  setup() {
    const invoices = ref([
      { id: 1, date: '2024-01-01', customer: 'Customer A', total: '$100' },
      { id: 2, date: '2024-02-15', customer: 'Customer B', total: '$200' }
      // بيانات مؤقتة أخرى
    ]);

    const viewInvoice = (invoice) => {
      // عرض تفاصيل الفاتورة مؤقتًا
      ElMessage.info(`Viewing Invoice ID: ${invoice.id}`);
    };

    const deleteInvoice = (id) => {
      // حذف الفاتورة مؤقتًا
      invoices.value = invoices.value.filter(invoice => invoice.id !== id);
      ElMessage.success('Invoice deleted successfully');
    };

    const addInvoice = () => {
      // إضافة فاتورة جديدة مؤقتًا
      const newInvoice = {
        id: invoices.value.length + 1,
        date: '2024-03-10',
        customer: `Customer ${String.fromCharCode(64 + invoices.value.length + 1)}`,
        total: `$${100 * (invoices.value.length + 1)}`
      };
      invoices.value.push(newInvoice);
      ElMessage.success('Invoice added successfully');
    };

    return {
      invoices,
      viewInvoice,
      deleteInvoice,
      addInvoice
    };
  }
};
</script>

<style scoped>
.invoices {
  padding: 20px;
}
</style>
