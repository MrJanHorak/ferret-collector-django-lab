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
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('ferrets/<int:ferret_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('ferrets/<int:ferret_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]