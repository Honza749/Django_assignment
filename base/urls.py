from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.get_all_data, name="detail data"),
    path(
        "detail/<str:model_name>/<str:object_id>",
        views.get_by_name_id,
        name="detail data by id",
    ),
    path("detail/<str:model_name>/", views.get_by_name, name="detail data by id"),
    re_path("^import/?$", views.process_import, name="add data"),
]
