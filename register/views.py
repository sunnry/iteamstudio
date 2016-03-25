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
        #if you want to redirect to customer url when signup successfully,you can set following value
        redirect_field_value = "/"
        ret.update({"redirect_field_value":redirect_field_value})
        return ret


c_signup = CustomerSignupView.as_view()
