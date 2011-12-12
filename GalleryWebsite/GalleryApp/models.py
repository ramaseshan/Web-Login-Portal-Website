from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.in_.forms import INStateSelect , INZipCodeField
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    street_address=models.CharField(maxlength=400)
    state=INStateSelect()
    zip_code=INZipCodeField()
    mobile_phone=models.CharField(max_length=10)
    avtar=models.ImageField
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=User)

    


# Create your models here.
