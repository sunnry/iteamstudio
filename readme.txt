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
