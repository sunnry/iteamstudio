from django import template
from django.core.files.storage import default_storage
from django.conf import settings

register = template.Library()

@register.filter(name='file_exists')

def file_exists(user_id):
    basepath = '/user_avatar/' + str(user_id) + '/avatar.jpg'
    filepath = settings.MEDIA_ROOT + basepath

    if default_storage.exists(filepath):
        return '/media' + basepath
    else:
        return '/media/user_avatar/default/default_avatar.png'

