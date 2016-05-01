from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class aboutView(TemplateView):
    template_name = 'about/about.html';


about_us = aboutView.as_view()
