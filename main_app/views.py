from django.shortcuts import render, redirect
from .models import Ferret
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def ferrets_index(request):
  ferrets = Ferret.objects.all()
  return render(request, 'ferrets/index.html', {'ferrets': ferrets})

def ferrets_detail(request, ferret_id):
  ferret = Ferret.objects.get(id = ferret_id)
  return render(request, 'ferrets/detail.html', {'ferret': ferret})

class FerretCreate(CreateView):
  model = Ferret
  fields = '__all__'

class FerretUpdate(UpdateView):
  model = Ferret
  fields = ['breed', 'description', 'age']

class FerretDelete(DeleteView):
  model = Ferret
  success_url = '/ferrets/'
