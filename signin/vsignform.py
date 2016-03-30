from allauth.account.forms import LoginForm
from django import forms


# you can customize your own form in this way,add a new field, the name
# need to match you template form field name
class vform(LoginForm):
    def __init__(self,*args,**kwargs):
        super(vform,self).__init__(*args,**kwargs)
        verify_field = forms.CharField()
        self.fields['imageVerify'] = verify_field

