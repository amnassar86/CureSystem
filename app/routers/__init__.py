from .patients import router as patients_router
from .employees import router as employees_router
from .invoices import router as invoices_router
from .sales import router as sales_router
from .suppliers import router as suppliers_router
from .cash_register import router as cash_register_router
from .transactions import router as transactions_router
from .prescriptions import router as prescriptions_router
from .pharmacy import router as pharmacy_router
from .payments import router as payments_router
from .permissions import router as permissions_router
from .roles import router as roles_router
from .role_permissions import router as role_permissions_router
from .shifts import router as shifts_router
from .user_roles import router as user_roles_router
from .medications import router as medications_router
from .category import router as category_router
from .sub_category import router as sub_category_router
from .customers import router as customers_router
from .doctors import router as doctors_router
from .notifications import router as notifications_router
from .audit_logs import router as audit_logs_router
from .archived_invoices import router as archived_invoices_router

__all__ = [
    "patients_router",
    "employees_router",
    "invoices_router",
    "sales_router",
    "suppliers_router",
    "cash_register_router",
    "transactions_router",
    "prescriptions_router",
    "pharmacy_router",
    "payments_router",
    "permissions_router",
    "roles_router",
    "role_permissions_router",
    "shifts_router",
    "user_roles_router",
    "medications_router",
    "category_router",
    "sub_category_router",
    "customers_router",
    "doctors_router",
    "notifications_router",
    "audit_logs_router",
    "archived_invoices_router",
]
