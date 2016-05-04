from django import forms
from django.core.mail import send_mail
from allauth.utils import set_form_field_order

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(max_length=50,required=True)
    contact_details = forms.CharField(max_length=1000,required=True)

    def __init__(self,*args,**kwargs):
        super(ContactUsForm,self).__init__(*args,**kwargs)
        set_form_field_order(self,["name","email","contact_details"])


    def is_valid(self):
        ret = super(ContactUsForm,self).is_valid()
        return ret


    def send(self,request):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['contact_details']
        send_mail(name,message,email,['sunhaihuan@gmail.com'],fail_silently=False)




