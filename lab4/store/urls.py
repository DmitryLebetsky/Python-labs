from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
     path('', views.realty_list, name='realty_list'),
     path('<int:id>', views.realty_detail,
          name='realty_detail'),
     path("create/", views.realty_create),
     path("edit/<int:id>/", views.realty_edit),
     path("delete/<int:id>/", views.realty_delete),
     path('<str:realty_type_name>/', views.realty_list,
          name='realty_list_by_category'
          ),
]