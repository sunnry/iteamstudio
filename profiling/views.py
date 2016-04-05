from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse,reverse_lazy
from allauth.account.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    @method_decorator(login_required(login_url='/signin'))
    def dispatch(self,*args,**kwargs):
        return super(ProfileView,self).dispatch(*args,**kwargs)


    def get_context_data(self, **kwargs):
        ret = super(ProfileView,self).get_context_data(**kwargs)
        try:
            tab = self.request.GET.get('tab')
            if isinstance(tab,unicode):
                tab = tab.encode('ascii','ignore')
            ret.update({'tab':tab})
            return ret
        except KeyError:
            return ret

        return ret


profiling = ProfileView.as_view()


class CustomerPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profiling:user_changepassword')

    @method_decorator(login_required(login_url='/signin'))
    def dispatch(self,request,*args,**kwargs):
        if not request.user.has_usable_password():
            return HttpResponseRedirect(reverse('account_set_password'))
        return super(PasswordChangeView,self).dispatch(request,*args,**kwargs)


    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordChangeView,self).get_context_data(**kwargs)
        ret.update({'tab':'changepassword'})
        return ret

changepassword = CustomerPasswordChangeView.as_view()


class CustomerPasswordResetView(PasswordResetView):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profiling:user_resetpassword_done')

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword'})
        return ret


resetpassword = CustomerPasswordResetView.as_view()


class CustomerPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/profile.html'

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetDoneView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword_done'})
        return ret

resetpassword_done = CustomerPasswordResetDoneView.as_view()
