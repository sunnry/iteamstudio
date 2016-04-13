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

class BaseProfileClass(object):
    def get_displayName(self):
        if self.request.user.is_authenticated():
            try:
                account = UserAccount.objects.get(user_id=self.request.user)
                username = getattr(account,'user_displayname')
                if isinstance(username,unicode):
                    username = username.encode('ascii','ignore')
                if username == '':
                    username = self.request.user.get_username()
                return username
            except UserAccount.DoesNotExist:
                    username = self.request.user.get_username()
                    return username
        else:
            return ""

    def get_useraccount_data(self,ctx):
        ret = ctx
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
                    'user_interest':user_interest,
                    'username':self.get_displayName()
                })
            except UserAccount.DoesNotExist:
                pass

        return ret


class ProfileView(TemplateView,BaseProfileClass):
    template_name = 'accounts/profile.html'

    @method_decorator(login_required(login_url='/signin'))
    def dispatch(self,*args,**kwargs):
        return super(ProfileView,self).dispatch(*args,**kwargs)

    def get_context_data(self, **kwargs):
        ret = super(ProfileView,self).get_context_data(**kwargs)
        tab = self.request.GET.get('tab')
        if tab != None:
            if isinstance(tab,unicode):
                tab = tab.encode('ascii','ignore')
            ret.update({'tab':tab})

        ret = self.get_useraccount_data(ret)

        return ret


profiling = ProfileView.as_view()


class CustomerPasswordChangeView(PasswordChangeView,BaseProfileClass):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profiling:user_changepassword')

    @method_decorator(login_required(login_url='/signin'))
    def dispatch(self,request,*args,**kwargs):
        if not request.user.has_usable_password():
            return HttpResponseRedirect(reverse('account_set_password'))
        return super(PasswordChangeView,self).dispatch(request,*args,**kwargs)


    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordChangeView,self).get_context_data(**kwargs)
        ret.update({'tab':'changepassword',
                    'username':self.get_displayName()
        })
        return ret

changepassword = CustomerPasswordChangeView.as_view()


class CustomerPasswordResetView(PasswordResetView,BaseProfileClass):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profiling:user_resetpassword_done')

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword',
                    'username':self.get_displayName()
        })
        return ret


resetpassword = CustomerPasswordResetView.as_view()


class CustomerPasswordResetDoneView(PasswordResetDoneView,BaseProfileClass):
    template_name = 'accounts/profile.html'

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetDoneView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword_done',
                    'username':self.get_displayName()
                })
        return ret

resetpassword_done = CustomerPasswordResetDoneView.as_view()




class CustomerPasswordResetFromKeyView(PasswordResetFromKeyView,BaseProfileClass):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('signin:signin')

    def get_context_data(self,**kwargs):
        ret = super(CustomerPasswordResetFromKeyView,self).get_context_data(**kwargs)
        ret.update({'tab':'resetpassword_from_key',
                    'username':self.get_displayName()
        })
        return ret

resetpassword_from_key = CustomerPasswordResetFromKeyView.as_view()

class UpdateUserProfileView(AjaxCapableProcessFormViewMixin,FormView,BaseProfileClass):
    template_name = 'accounts/profile.html'
    form_class = ProfileForm
    redirect_field_name = 'next'
    success_url = reverse_lazy('index:index')
    ferrors = None

    def dispatch(self,request,*args,**kwargs):
        return super(UpdateUserProfileView,self).dispatch(request,*args,**kwargs)

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,'user_profile',self.form_class)

    def form_valid(self,form):
        if form.save(self.request):
            return HttpResponseRedirect(reverse('profiling:user_profile'))
        else:
            return HttpResponseRedirect(reverse('profiling:user_profile')) #next commit will redirect to error page

    def form_invalid(self,form):
        ctx = self.get_context_data()
        ctx = self.export_error(form,ctx)
        return self.render_to_response(ctx)

    def export_error(self,form,ctx):
        ret = ctx
        if form._errors:
            try:
                avatar_error = form._errors.pop('avatar')
                ret.update({'avatar_error':avatar_error})
            except KeyError:
                pass
            try:
                display_username_error = form._errors.pop('display_username')
                ret.update({'display_username_error':display_username_error})
            except KeyError:
                pass
            try:
                phone_error = form._errors.pop('phone')
                ret.update({'phone_error':phone_error})
            except KeyError:
                pass
            try:
                location_error = form._errors.pop('location')
                ret.update({'location_error':location_error})
            except KeyError:
                pass
            try:
                interest_error = form._errors.pop('interest')
                ret.update({'interest_error':interest_error})
            except KeyError:
                pass
            try:
                gender_error = form._errors.pop('gender')
                ret.update({'gender_error':gender_error})
            except KeyError:
                pass
        return ret

    def get_context_data(self,**kwargs):
        ret = super(UpdateUserProfileView,self).get_context_data(**kwargs)
        ret.update({'tab':'basic',
                    'username':self.get_displayName()
        })
        ret = self.get_useraccount_data(ret)
        return ret

updateprofile = UpdateUserProfileView.as_view()
