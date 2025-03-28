from django.urls import path
from . import views
app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'), #전체 게시글
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
]
