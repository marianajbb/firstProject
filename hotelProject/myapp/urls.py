from django.urls import path
from .views import employee_list, employee_create, employee_update, employee_delete

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create/', employee_create, name='employee_create'),
    path('update/<str:employee_id>/', employee_update, name='employee_update'),
    path('delete/<str:employee_id>/', employee_delete, name='employee_delete'),
]