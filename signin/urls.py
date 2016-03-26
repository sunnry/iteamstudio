from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.c_signin,name="signin"),
]
