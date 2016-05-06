"""iteamstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', include('index.urls',namespace="index")),
    url(r'^register/',include('register.urls',namespace="register")),
    url(r'^signin/',include('signin.urls',namespace="signin")),
    url(r'^lang/$','index.views.multilanguages',name='multilanguages'),
    url(r'^about/$','about.views.about_us',name='about_us'),
    url(r'^contact/$','about.views.contact_us',name='contact_us'),
    url(r'^cases/$','about.views.cases',name='cases'),
    url(r'^accounts/signup/$','register.views.c_signup',name = 'customerSignup'),
    url(r'^accounts/login/$','signin.views.c_signin',name = 'customerSignin'),
    url(r'^accounts/captcha/$','signin.views.captcha',name = 'captcha'),
    url(r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$','profiling.views.resetpassword_from_key',name='resetpassword_from_key'),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^accounts/profile/',include('profiling.urls',namespace='profiling')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
