from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name=''),
    path('<int:post_id>/', views.article, name='article'),
    path('create', views.create, name='create'),

]