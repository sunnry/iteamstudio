from django import forms
from .models import UserAccount
from allauth.utils import set_form_field_order
import pdb


class ProfileForm(forms.Form):
    phone = forms.IntegerField()
    display_username = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    interest = forms.CharField(max_length=500)
    gender = forms.CharField(max_length=7)
    user = None

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        set_form_field_order(self,["phone","display_username","location","interest","gender"])

    #this function is used to bound data with form, i do nothing here just inherit from super class
    #to get error information
    def is_valid(self):
        ret = super(ProfileForm,self).is_valid()
        if not ret:
            e = self._errors
            pdb.set_trace()

        return ret

    #this is form clean, will be called by super class,i do nothing here,just for debugging,but you
    #can add your additional clean code
    def clean(self):
        super(ProfileForm,self).clean()
        if self._errors:
            #pdb.set_trace()
            return
        return self.cleaned_data

    def save(self,request):
        if request.user.is_authenticated():
            self.user = request.user
            p = self.cleaned_data['phone']
            d = self.cleaned_data['display_username']
            l = self.cleaned_data['location']
            i = self.cleaned_data['interest']
            g = self.cleaned_data['gender']
            account = UserAccount(user=self.user,user_displayname=d,user_phone=p,user_location=l,user_interest=i,user_gender=g)
            account.save()
            return True

        return False
