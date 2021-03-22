import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from fleif.objects import Country, get_country_name

code = 'AD'
c = Country(code)
print(c.name)

print(get_country_name(code))
