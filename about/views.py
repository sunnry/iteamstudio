from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from allauth.account.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetFromKeyView,RedirectAuthenticatedUserMixin,AjaxCapableProcessFormViewMixin
from .forms import ContactUsForm
#import pdb
# Create your views here.


class aboutView(TemplateView):
    template_name = 'about/about.html';


about_us = aboutView.as_view()



class contactView(AjaxCapableProcessFormViewMixin,FormView):
    template_name = 'about/about.html';
    form_class = ContactUsForm

    def get_from_class(self):
        return get_form_class(app_settings.FORMS,'contactForm',self.form_class)

    def form_valid(self,form):
        form.send(self.request)
        ctx = self.get_context_data()
        ctx.update({'send_success':'this message has send successfully!'})
        return self.render_to_response(ctx)

    def form_invalid(self,form):
        ctx = self.get_context_data()

        if form._errors:
            try:
                name_error = form._errors.pop('name')
                ctx.update({'name_error':name_error})
            except KeyError:
                pass

            try:
                email_error = form._errors.pop('email')
                ctx.update({'email_error':email_error})
            except KeyError:
                pass

            try:
                contact_details_error = form._errors.pop('contact_details_error')
                ctx.update({'contact_details_error':contact_details_error})
            except KeyError:
                pass

        return self.render_to_response(ctx)

    def get_context_data(self,**kwargs):
        ret = super(contactView,self).get_context_data(**kwargs)
        return ret

contact_us = contactView.as_view()
