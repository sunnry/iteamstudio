from allauth.account.forms import SignupForm
from django import forms


class vSignupForm(SignupForm):
    def __init__(self,*args,**kwargs):
        super(vSignupForm,self).__init__(*args,**kwargs)
        verify_field = forms.CharField()
        self.fields['imageVerify'] = verify_field
