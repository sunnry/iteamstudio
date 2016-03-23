from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    @method_decorator(login_required(login_url='/signin'))
    def dispatch(self,*args,**kwargs):
        return super(ProfileView,self).dispatch(*args,**kwargs)



profiling = ProfileView.as_view()

