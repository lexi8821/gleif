import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from fleif.search import fuzzysearch, autocomplete

phrase = 'ceska'

print(autocomplete(phrase))
print(50*'-')
print(fuzzysearch(phrase))
