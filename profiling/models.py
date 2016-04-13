from django.db import models
from django.conf import settings
from os.path import basename

# Create your models here.

def get_upload_path(instance,filename):
    return instance._get_upload_path(filename)

class UserAccount(models.Model):
#    user_logo_file = models.FileField()
#    user_avatar = models.FileField(upload_to='user_avatar/%Y/%m/%d')
    user_avatar = models.FileField(upload_to=get_upload_path,blank=True)
    user_displayname = models.CharField(max_length=30,blank=True)
#    user_email = models.EmailField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    user_phone = models.CharField(max_length=30,blank=True)
    user_location = models.CharField(max_length=30)
    user_interest = models.TextField()

    UN = 'UN'
    FE = 'FE'
    MA = "MA"
    GENDER_CHOICES = (
        (UN,'unknown'),
        (FE,'female'),
        (MA,'male'),
    )
    user_gender = models.CharField(max_length=2,choices=GENDER_CHOICES,
                                   default=UN)

    def _get_upload_path(self,filename):
        b = basename(filename)
        return "user_avatar/" + str(self.user.id) + "/avatar.jpg"
