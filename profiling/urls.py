from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.profiling,name="user_profile"),
        url(r'^changepassword/$',views.changepassword,name="user_changepassword"),
]
