from django.shortcuts import render
from .models import Ferret


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

