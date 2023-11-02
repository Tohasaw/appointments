from django.urls import path
from Appointments.views import apps_customer_new, apps_employee_list, apps_customer_gettime, apps_customer_getdate

urlpatterns = [
    path('apps/employee/list', apps_employee_list, name='apps_employee_list'),
    #path('apps/list', apps_customer_list, name='apps_customer_list'),
    path('apps/new', apps_customer_new, name='apps_customer_new'),
    path('apps/date', apps_customer_getdate, name='apps_employee_list'),
    path('apps/time', apps_customer_gettime, name='apps_customer_gettime'),
]