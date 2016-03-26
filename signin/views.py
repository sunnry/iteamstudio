from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allauth.account.views import LoginView

# Create your views here.

def signin(request):
        template = loader.get_template('signin/signin.html')
        context = {}
        return HttpResponse(template.render(context,request))



class CustomerSigninView(LoginView):
    template_name = "signin/signin.html"

    def get_context_data(self,**kwargs):
        ret = super(CustomerSigninView,self).get_context_data(**kwargs)
        redirect_field_value = "/"
        ret.update({'redirect_field_value':redirect_field_value})
        return ret

c_signin = CustomerSigninView.as_view()
