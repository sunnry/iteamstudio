debug method:

1. use pdb module
   1.1 you can import pdb module in python file and calling pdb.set_trace() at related place,then the python will stop at this place.

   1.2 you can debug one python file dirctly.
   #python -m pdb myscript.py


get information of one python module

1. you can use python help command after you import this module:
   >>> import django
   >>> help(django)
