from django.urls import path
from . import views

urlpatterns = [
    path('', views.getIns, name= "all options"),
    path('allData/', views.allData, name="detail data"),
    path('detail/<str:pk>/', views.detail_by_id, name="detail data bz id"),
    path('import/', views.addData, name="add data"),
    path('delete/<str:pk>/', views.delete, name="odstranit"),

]