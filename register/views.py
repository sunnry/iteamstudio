from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allauth.account.views import SignupView
# Create your views here.


def register(request):
        template = loader.get_template('register/register.html')
        context = {}
        return HttpResponse(template.render(context,request))



class CustomerSignupView(SignupView):
    template_name = "register/register.html"

    def get_context_data(self,**kwargs):
        ret = super(CustomerSignupView,self).get_context_data(**kwargs)
        return ret


c_signup = CustomerSignupView.as_view()
# Create your views here.
