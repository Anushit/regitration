from django.urls import path
from . import views

urlpatterns = [
    path('Employee/', views.EmployeeList, name="Employee"),
    path('Employee/detail/<str:pk>/', views.Employeedetail, name="detail"),
    path('Employee/create/', views.EmployeeCreate, name="create"),
    path('Employee/update/<str:pk>/', views.EmployeeUpdate, name="update"),
    path('Employee/delete/<str:pk>/', views.EmployeeUpdate, name="delete"),


    ]