from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('ferrets/', views.ferrets_index, name='ferrets_index'),
]