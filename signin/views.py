from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allauth.account.views import LoginView

from PIL import Image,ImageDraw,ImageFont
import cStringIO,random,string,os
from iteamstudio.settings import BASE_DIR

from .vsignform import vform
from django import forms
# Create your views here.


def captcha(request):
    image = Image.new('RGB',(120,34),color=(255,255,255))
    draw = ImageDraw.Draw(image)
    font_file = os.path.join(BASE_DIR,'static/assets/fonts/vinking_n.ttf')
    font = ImageFont.truetype(font_file,28)
    random_str = ''.join(random.sample(string.letters + string.digits,4))
    draw.text((4,4),random_str,fill=(0,0,0),font=font)
    del draw
    #store random string to session for later compare
    request.session['captha'] = random_str.lower()
    buf = cStringIO.StringIO()
    image.save(buf,'jpeg')
    return HttpResponse(buf.getvalue(),'image/jpeg')



def signin(request):
        template = loader.get_template('signin/signin.html')
        context = {}
        return HttpResponse(template.render(context,request))



class CustomerSigninView(LoginView):
    template_name = "signin/signin.html"
    form_class = vform

    def get_form_class(self):
        return super(LoginView,self).get_form_class()

    def form_invalid(self,form):
        try:
            vcode = form.cleaned_data['imageVerify'].lower()
        except KeyError:
            ctx = self.get_context_data()
            error_code = "verify code empty"
            ctx.update({'imageVerifyError':error_code})
            return self.render_to_response(ctx)

        return super(CustomerSigninView,self).form_invalid(form)



    def form_valid(self,form):
        vcode = form.cleaned_data['imageVerify'].lower()
        vcode_session = self.request.session['captha']

        if isinstance(vcode,unicode):
            vcode = vcode.encode('ascii','ignore')

        if isinstance(vcode_session,unicode):
            vcode_session = vcode_session.encode('ascii','ignore')

        #if image verify code correct, following into normal login process
        if vcode == vcode_session:
            return super(CustomerSigninView,self).form_valid(form)
        else:
            ctx = self.get_context_data()
            error_code = 'verify code not match'
            ctx.update({'imageVerifyError':error_code})
            return self.render_to_response(ctx)


    def get_context_data(self,**kwargs):
        ret = super(CustomerSigninView,self).get_context_data(**kwargs)
        redirect_field_value = "/"
        ret.update({'redirect_field_value':redirect_field_value})
        return ret

c_signin = CustomerSigninView.as_view()
