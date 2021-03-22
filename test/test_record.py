import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from gleif.record import Record, Entity
from gleif.downloader import Downloader
from gleif import BASE_URL, L1_ENDPOINTS
from pprint import pprint

lei_no = 'IYKCAVNFR8QGF00HV840'
lei_no = '549300DS86PEHLIYB473'
r = Record(lei_no)

#url = f"{BASE_URL}/{L1_ENDPOINTS[0]}/{lei_no}"
#print(url)
#d = Downloader(url)
#url = d.data[0]['relationships']['direct-parent']['links']['related']
#print(url)
#f = Downloader(url)
