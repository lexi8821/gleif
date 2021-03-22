import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from gleif.objects import LeiIssuer


code = '029200067A7K6CH0H586'
li = LeiIssuer(code)

print(f"Name: {li.name}")
print(f"Jurisdiction: {li.jurisdiction}")
