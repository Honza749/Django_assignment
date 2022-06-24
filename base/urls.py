from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.getIns, name= "all options"),
    path('get_all', views.allData, name="detail data"),

    path('detail/<str:model_name>/<str:object_id>', views.get_by_name_id, name="detail data by id"),
    path('detail/<str:model_name>/', views.get_by_name, name="detail data by id"),
    re_path('^import/?$', views.append_object, name='add data')
]