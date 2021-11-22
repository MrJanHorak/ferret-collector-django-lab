from django.contrib import admin
from .models import Ferret, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Ferret)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)

