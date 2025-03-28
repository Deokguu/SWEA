from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), #전체 게시글
    path('<int:pk>/', views.detail, name='detail'), # 각각의 단일 게시물
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete')
]
