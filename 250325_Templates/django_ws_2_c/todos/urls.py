from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [

    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='creat_todo'),
    path('<str:work>/', views.detail, name='detail')
]
