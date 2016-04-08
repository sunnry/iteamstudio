from django.db import models
from django.conf import settings

# Create your models here.


class UserAccount(models.Model):
#    user_logo_file = models.FileField()
    user_displayname = models.CharField(max_length=30)
#    user_email = models.EmailField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    user_phone = models.IntegerField(null=True,blank=True)
    user_location = models.CharField(max_length=30)
    user_interest = models.TextField(blank=True)

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
