from django.shortcuts import render, redirect
from .models import Ferret, Toy, Photo
from .forms import FeedingsForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'my-very-happy-ferret-collector'

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
  toys_ferret_doesnt_have = Toy.objects.exclude(id__in = ferret.toys.all().values_list('id'))
  feeding_form = FeedingsForm()
  return render(request, 'ferrets/detail.html', {'ferret': ferret, 'feeding_form': feeding_form, 'toys': toys_ferret_doesnt_have})

def add_feeding(request, ferret_id):
  form = FeedingsForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.ferret_id = ferret_id
    new_feeding.save()
  return redirect('ferrets_detail', ferret_id=ferret_id)

def assoc_toy(request, ferret_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Ferret.objects.get(id=ferret_id).toys.add(toy_id)
  return redirect('ferrets_detail', ferret_id=ferret_id)

def deassoc_toy(request, ferret_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Ferret.objects.get(id=ferret_id).toys.remove(toy_id)
  return redirect('ferrets_detail', ferret_id=ferret_id)

def add_photo(request, ferret_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, ferret_id=ferret_id)
      ferret_photo = Photo.objects.filter(ferret_id=ferret_id)
      if ferret_photo.first():
        ferret_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occured uploading file to S3: %s' % err)
  return redirect('ferrets_detail', ferret_id=ferret_id)

class FerretCreate(CreateView):
  model = Ferret
  fields = ['name', 'breed', 'description', 'age']

class FerretUpdate(UpdateView):
  model = Ferret
  fields = ['breed', 'description', 'age']

class FerretDelete(DeleteView):
  model = Ferret
  success_url = '/ferrets/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'