from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse,reverse_lazy
from allauth.account.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetFromKeyView,RedirectAuthenticatedUserMixin,AjaxCapableProcessFormViewMixin
from allauth.utils import get_form_class
from allauth.account import app_settings
from .forms import ProfileForm
from .models import UserAccount
import pdb

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

            if self.request.user.is_authenticated():
                try:
                    p = UserAccount.objects.get(user_id=self.request.user)
                    user_displayname = getattr(p,'user_displayname')
                    user_phone = getattr(p,'user_phone')
                    user_location = getattr(p,'user_location')
                    user_interest = getattr(p,'user_interest')
                    ret.update({
                        'user_displayname':user_displayname,
                        'user_phone':user_phone,
                        'user_location':user_location,
                        'user_interest':user_interest
                    })
                    #pdb.set_trace()
                    return ret
                except UserAccount.DoesNotExist:
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




class CustomerPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('signin:signin')

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetFromKeyView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword_from_key'})
        return ret

resetpassword_from_key = CustomerPasswordResetFromKeyView.as_view()

class UpdateUserProfileView(AjaxCapableProcessFormViewMixin,FormView):
    template_name = 'accounts/profile.html'
    form_class = ProfileForm
    redirect_field_name = 'next'
    success_url = reverse_lazy('index:index')

    def dispatch(self,request,*args,**kwargs):
        return super(UpdateUserProfileView,self).dispatch(request,*args,**kwargs)

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,'user_profile',self.form_class)

    def form_valid(self,form):
        if form.save(self.request):
            return HttpResponseRedirect(reverse('profiling:user_profile'))
        else:
            return HttpResponseRedirect(reverse('index:index')) #next commit will redirect to error page

    def form_invalid(self,form):
        return HttpResponseRedirect(reverse('index:index')) #next commit will redirect to error page

    def get_context_data(self,**kwargs):
        ret = super(UpdateUserProfileView,self).get_context_data(**kwargs)
        ret.update({'tab':'basic'})
        return ret

updateprofile = UpdateUserProfileView.as_view()
