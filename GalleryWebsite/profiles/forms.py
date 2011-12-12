from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from GalleryWebsite.profiles.models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= ('gender','profilepic','birth_date','address','city','state','pincode')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')