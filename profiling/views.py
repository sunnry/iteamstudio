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

