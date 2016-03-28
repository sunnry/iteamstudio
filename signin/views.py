from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allauth.account.views import LoginView

from PIL import Image,ImageDraw,ImageFont
import cStringIO,random,string,os
from iteamstudio.settings import BASE_DIR
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

    def get_context_data(self,**kwargs):
        ret = super(CustomerSigninView,self).get_context_data(**kwargs)
        redirect_field_value = "/"
        ret.update({'redirect_field_value':redirect_field_value})
        return ret

c_signin = CustomerSigninView.as_view()
