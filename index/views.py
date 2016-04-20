from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic.base import TemplateView
from profiling.models import UserAccount
from django.core.urlresolvers import reverse,reverse_lazy

# Create your views here.

def multilanguages(request):
    lan = request.GET.get('lan')
    if isinstance(lan,unicode):
        lan = lan.encode('ascii','ignore')
    request.session['lan'] = lan
    return HttpResponseRedirect(reverse('index:index'))

def indexPage(request):
	template = loader.get_template('index/index.html')
	context = {}
	return HttpResponse(template.render(context,request))


class HomePageIndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self,**kwargs):
        ret = super(HomePageIndexView,self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            try:
                account = UserAccount.objects.get(user_id=self.request.user)
                username = getattr(account,'user_displayname')
                if isinstance(username,unicode):
                    username = username.encode('ascii','ignore')
                if username == '':
                    username = self.request.user.get_username()
                ret.update({'username':username})
            except UserAccount.DoesNotExist:
                username = self.request.user.get_username()
                if isinstance(username,unicode):
                    username = username.encode('ascii','ignore')
                ret.update({'username':username})

        return ret


index = HomePageIndexView.as_view()
