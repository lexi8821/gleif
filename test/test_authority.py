import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from gleif.objects import RegistrationAuthority

authority_no = 'RA000006'
r = RegistrationAuthority(authority_no)
print(f"Authority Code: {r.code}")
print(f"Authority Name: {r.internationalName}")
print(f"Authority Country: {r.jurisdiction}")
print(f"Authority website: {r.website}")
