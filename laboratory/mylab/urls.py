from django.urls import path

from . import views

app_name = 'mylab'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:post_type>/', views.category, name='category'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('post_modify/<int:post_id>/', views.post_modify, name='post_modify'),
    # path('post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
]