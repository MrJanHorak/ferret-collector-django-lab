from django.db.models.base import Model
from django.forms import ModelForm
from .models import Feeding

class FeedingsForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date','meal']

    