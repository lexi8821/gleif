import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from gleif.objects import LegalForm

entity_code = 'D8XQ'
entity_code = '9HLU'
r = LegalForm(entity_code)
print(r)
