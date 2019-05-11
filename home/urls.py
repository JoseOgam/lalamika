from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.index_view, name='index'),


]
