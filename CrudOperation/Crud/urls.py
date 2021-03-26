from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('api/', views.artistList,name="artist"),
    path('api/detail/<str:pk>/', views.artistdetail, name="detail"),
    path('api/create/',views.artistCreate,name="create"),
    path('api/update/<str:pk>/',views.artistUpdate,name="update"),
    path('api/delete/<str:pk>/',views.artistDelete,name="delete"),
    #path('EmployeeView/',views.EmployeeView.as_view(),name="EmployeeView"),
    ]


