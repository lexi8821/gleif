import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from fleif.objects import Jurisdiction, get_jurisdiction_name

code = 'AD'
j = Jurisdiction(code)
print(f"Jurisdiction name: {j.name}")
print(f"Jurisdiction code: {j.code}")

print(get_jurisdiction_name('CZ'))
