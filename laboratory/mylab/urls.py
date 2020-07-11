from django.urls import path

from . import views

app_name = 'mylab'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
]