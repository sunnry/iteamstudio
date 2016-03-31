from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allauth.account.views import SignupView

from .vsignupform import vSignupForm
from django import forms
# Create your views here.

def register(request):
        template = loader.get_template('register/register.html')
        context = {}
        return HttpResponse(template.render(context,request))



class CustomerSignupView(SignupView):
    template_name = "register/register.html"
    form_class = vSignupForm

    def form_invalid(self,form):
        try:
            vcode = form.cleaned_data['imageVerify'].lower()
        except KeyError:
            ctx = self.get_context_data(form=form)
            error_code = 'verify code empty'
            ctx.update({'imageVerifyError':error_code})
            return self.render_to_response(ctx)
        return super(CustomerSignupView,self).form_invalid(form)

    def form_valid(self,form):
        vcode = form.cleaned_data['imageVerify'].lower()
        vcode_session = self.request.session['captha']

        if isinstance(vcode,unicode):
            vcode = vcode.encode('ascii','ignore')

        if isinstance(vcode_session,unicode):
            vcode_session = vcode_session.encode('ascii','ignore')

        if vcode == vcode_session:
            return super(CustomerSignupView,self).form_valid(form)
        else:
            ctx = self.get_context_data(form=form)
            error_code = 'verify code not match'
            ctx.update({'imageVerifyError':error_code})
            return self.render_to_response(ctx)


    def get_context_data(self,**kwargs):
        ret = super(CustomerSignupView,self).get_context_data(**kwargs)
        #if you want to redirect to customer url when signup successfully,you can set following value
        redirect_field_value = "/"
        ret.update({"redirect_field_value":redirect_field_value})
        return ret


c_signup = CustomerSignupView.as_view()
