import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from fleif.objects import Field, Fields


code = 'LEIREC_ADDRESSES_LINE_3'
fi = Fields()
ids = [i['id'] for i in fi.data]
for id in ids:
    f = Field(id)
    attribs = [att for att in dir(f) if not att.startswith('_') and not att == 'download']
    for att in attribs:
        print(att, ': ', getattr(f, att))
    print(50*'-')
