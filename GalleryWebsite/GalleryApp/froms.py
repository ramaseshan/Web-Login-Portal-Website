from django.db import models
from django.forms import ModelForm
from ourcrestmont.itaco.models import *
 
class ProfileForm(ModelForm):
    class Meta:
        model = "abhijeet"
        exclude = ('field1','field2','field3',)