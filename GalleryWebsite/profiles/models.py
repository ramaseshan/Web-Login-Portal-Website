from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def upload_path_handler(instance, filename):
    return "user_{id}/profileppics/{file}".format(id=instance.user.id, file=filename.replace('\\','/'))


class Profile(models.Model):
    """ Profile model """
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    user              = models.ForeignKey(User, unique=True)
    gender            = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    profilepic        = models.FileField(_('profilepic'), upload_to=upload_path_handler, blank=True)
    birth_date        = models.DateField(_('birth date'), blank=True, null=True)
    address           = models.CharField(_('address'), blank=True, max_length=200)
    city              = models.CharField(_('city'), blank=True, max_length=20)
    state             = models.CharField(_('state'), blank=True, max_length=25)
    pincode           = models.CharField(_('pincode'), blank=True, max_length=6)
    aboutme           = models.CharField(_('aboutme'), blank=True, max_length=500)
    photos            = models.IntegerField(_('photos'),default=0)
      
    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
        db_table = 'user_profiles'

    def __unicode__(self):
        return u"%s" % self.user.get_full_name()

    @permalink
    def get_absolute_url(self):
        return ('profile_detail', None, { 'username': self.user.username })

    
