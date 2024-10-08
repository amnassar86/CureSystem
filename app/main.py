# app/main.py
from fastapi import FastAPI
from app.models import (patients, 
      employees,
      invoices,
      sales,
      suppliers,
      cash_register,
      transactions,
      prescriptions,
      pharmacy,
      payments,
      permissions, 
      roles,
      role_permissions,
      shifts,
      user_roles,
      medications,
      category,
      sub_category,
      customers,
      doctors,
      notifications,
      audit_logs,
      archived_invoices,)
from app.routers import (
  patients,
  employees,
  invoices,
  sales,
  suppliers,
  cash_register,
  transactions,
  prescriptions,
  pharmacy,  # Added Pharmacy router
  payments,
  permissions,
  roles,
  role_permissions,
  shifts,
  user_roles,
  medications,
  category,
  sub_category,
  customers,
  doctors,
  notifications,
  audit_logs,
  archived_invoices,
)

app = FastAPI()  # احتفظ فقط بهذا التعريف

# تضمين المسارات (routers)
app.include_router(patients.router, prefix="/api/patients", tags=["Patients"])
app.include_router(employees.router, prefix="/api/employees", tags=["Employees"])
app.include_router(invoices.router, prefix="/api/invoices", tags=["Invoices"])
app.include_router(medications.router, prefix="/api/medications", tags=["Medications"])
app.include_router(sales.router, prefix="/api/sales", tags=["Sales"])
app.include_router(prescriptions.router, prefix="/api/prescriptions", tags=["Prescriptions"])
app.include_router(suppliers.router, prefix="/api/suppliers", tags=["Suppliers"])
app.include_router(pharmacy.router, prefix="/api/pharmacy", tags=["Pharmacy"])
app.include_router(shifts.router, prefix="/api/shifts", tags=["Shifts"])
app.include_router(cash_register.router, prefix="/api/cash_register", tags=["Cash Register"])
app.include_router(payments.router, prefix="/api/payments", tags=["Payments"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])
app.include_router(roles.router, prefix="/api/roles", tags=["Roles"])
app.include_router(permissions.router, prefix="/api/permissions", tags=["Permissions"])
app.include_router(role_permissions.router, prefix="/api/role_permissions", tags=["Role Permissions"])
app.include_router(user_roles.router, prefix="/api/user_roles", tags=["User Roles"])
app.include_router(category.router, prefix="/api/category", tags=["Category"])
app.include_router(sub_category.router, prefix="/api/sub_category", tags=["SubCategory"])
app.include_router(customers.router, prefix="/api/customers", tags=["Customers"])
app.include_router(doctors.router, prefix="/api/doctors", tags=["Doctors"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(audit_logs.router, prefix="/api/audit_logs", tags=["Audit Logs"])
app.include_router(archived_invoices.router, prefix="/api/archived_invoices", tags=["Archived Invoices"])







# تعريف فحص الصحة (health check)
@app.get("/health")
def health_check():
  return {"status": "ok"}
