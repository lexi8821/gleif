import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from fleif.objects import Region, get_region_name

code = 'AD-03'
r = Region(code)
print(r.name)

print(get_region_name(code))
