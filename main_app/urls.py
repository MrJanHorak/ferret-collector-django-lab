from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('ferrets/', views.ferrets_index, name='ferrets_index'),
  path('ferrets/<int:ferret_id>/', views.ferrets_detail, name='ferrets_detail'),
  path('ferrets/create/', views.FerretCreate.as_view(), name='ferrets_create'),
  path('ferrets/<int:pk>/update/', views.FerretUpdate.as_view(), name='ferrets_update'),
  path('ferrets/<int:pk>/delete/', views.FerretDelete.as_view(), name='ferrets_delete'),
  path('ferrets/<int:ferret_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]