#from lei.agent import RegistrationAgent, get_agent_name
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from gleif.objects import RegistrationAgent, get_agent_name

code = '5d10d4dc929ab6.72309473'
ra = RegistrationAgent(code)
print(ra.websites)
print(get_agent_name(code))
