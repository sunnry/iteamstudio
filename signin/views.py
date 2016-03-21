from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def signin(request):
        template = loader.get_template('signin/signin.html')
        context = {}
        return HttpResponse(template.render(context,request))



