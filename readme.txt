debug method:

1. use pdb module
   1.1 you can import pdb module in python file and calling pdb.set_trace() at related place,then the python will stop at this place.

   1.2 you can debug one python file dirctly.
   #python -m pdb myscript.py


get information of one python module

1. you can use python help command after you import this module:
   >>> import django
   >>> help(django)

2. install python plugin for vim : pydiction
   #git clone https://github.com/rkulla/pydiction.git
   #see readme of this repo, which will tell you how install and config pydiction plugin


3. the use of 'redirect_field_name' and 'redirect_field_value' in allauth module:
   	for example in allauth default signup template signup.html, the form has a hidden input
   value of 'next' when signup successfully with this default signup template, it will redirect
   to the url valued with 'redirect_field_value', if you set redirect_field_value to '\', when si   gnup successfully, it will redirect to '\', but if you want to use this feature you must add input element named with 'next' into your template, remember this.


requirements:
has developed in following environment:
#apt-get install nginx(1.4.6)
#apt-get install uwsgi(4.8.4)
#pip install django(1.8.9)
#pip install django-allauth(0.25.2)
#apt-get install python-mysqldb
#apt-get install libjpeg-dev
#pip install Pillow(2.3.0)

has deployed in following environment:
#apt-get install nginx(1.4.6)
#apt-get install uwsgi(2.0.13)
#pip install django(1.9.6)
#pip install django-allauth(0.25.2)
#apt-get install python-mysqldb
#apt-get install libjpeg-dev
#pip install Pillow(3.2.0)

