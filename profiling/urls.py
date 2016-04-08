from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.profiling,name="user_profile"),
        url(r'^updateprofile/$',views.updateprofile,name="updateprofile"),
        url(r'^changepassword/$',views.changepassword,name="user_changepassword"),
        url(r'^resetpassword/$',views.resetpassword,name="user_resetpassword"),
        url(r'^resetpassword_done/$',views.resetpassword_done,name="user_resetpassword_done"),
]
