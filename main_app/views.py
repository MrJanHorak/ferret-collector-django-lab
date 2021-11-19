from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

class Ferret:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

ferrets = [
  Ferret('Lolo', 'tabby', 'Kinda rude.', 3),
  Ferret('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Ferret('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Ferret('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Ferret Loving Friend!</h1>')


def about(request):
  return render(request, 'about.html')


def ferrets_index(request):
  return render(request, 'ferrets/index.html', {'ferrets': ferrets})