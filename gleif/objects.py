import os
from gleif.downloader import Downloader
from gleif.utils import load, save
from gleif import BASE_URL, L1_ENDPOINTS, L3_ENDPOINTS

class RegistrationAgents:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'agents.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating registration agents.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[10]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data[0]
        save(self.FILE, d.data[0])

class RegistrationAgent:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        ra = RegistrationAgents()
        codes = [i['id'] for i in ra.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached agents. Updating dataset.")
            ra.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No registration agent with the code {self.code}")
                return
        self.name = ra.data[p]['attributes']['name']
        self.lei = ra.data[p]['attributes']['lei']
        self.leiIssuer = ra.data[p]['attributes']['leiIssuer']
        self.websites = ra.data[p]['attributes']['websites'][0]

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[10]}/{self.code}"
        d = Downlaoder(url)
        self.name = d.data[0]['attributes']['name']
        self.lei = ra.data[0]['attributes']['lei']
        self.leiIssuer = ra.data[0]['attributes']['leiIssuer']
        self.websites = ra.data[0]['attributes']['websites'][0]

def get_agent_name(agent_code):
    j = RegistrationAgent(agent_code)
    return j.name

class RegistrationAuthorities:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'authorities.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating Registration Authorities.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[9]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class RegistrationAuthority():
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        ra = RegistrationAuthorities()
        codes = [i['attributes']['code'] for i in ra.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached authorities. Updating dataset.")
            ra.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No registration authority with the code {self.code}")
                return
        self.code = ra.data[p]['attributes']['code']
        self.internationalName = ra.data[p]['attributes']['internationalName']
        self.localName = ra.data[p]['attributes']['localName']
        self.InternationalorganizationName = ra.data[p]['attributes']['internationalOrganizationName']
        self.LocalOrganizationName = ra.data[p]['attributes']['localOrganizationName']
        self.website = ra.data[p]['attributes']['website']
        self.jurisdiction = ra.data[p]['attributes']['jurisdictions'][0]['countryCode']

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[9]}/{self.code}"
        d = Downlaoder(url)
        self.internationalName = d.data[0]['attributes']['internationalName']
        self.localName = d.data[0]['attributes']['localName']
        self.InternationalorganizationName = d.data[0]['attributes']['internationalOrganizationName']
        self.LocalOrganizationName = d.data[0]['attributes']['localOrganizationName']
        self.website = d.data[0]['attributes']['website']
        self.jurisdiction = d.data[0]['attributes']['jurisdictions'][0]['countryCode']

class Countries:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'countries.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating countries.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[5]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class Country:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        c = Countries()
        codes = [i['id'] for i in c.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached countries. Updating dataset.")
            c.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No country with the code {self.code}")
                return
        self.name = c.data[p]['attributes']['name']

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[5]}/{self.code}"
        d = Downlaoder(url)
        self.name = d.data[0]['attributes']['name']

def get_country_name(country_code):
    j = Country(country_code)
    return j.name

class Jurisdictions:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'jurisdictions.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating jurisdictions.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[7]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class Jurisdiction:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        j = Jurisdictions()
        codes = [i['attributes']['code'] for i in j.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached jurisdictions. Updating dataset.")
            ra.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No jurisdiction with the code {self.code}")
                return
        self.name = j.data[p]['attributes']['name']

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[7]}/{self.code}"
        d = Downlaoder(url)
        self.name = d.data[0]['attributes']['name']

def get_jurisdiction_name(jurisdiction_code):
    j = Jurisdiction(jurisdiction_code)
    return j.name

class Fields:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'fields.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating fields.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[4]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class Field:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        f = Fields()
        codes = [i['id'] for i in f.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached countries. Updating dataset.")
            f.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No country with the code {self.code}")
                return
        for k in list(f.data[p]['attributes'].keys()):
            setattr(self, k, f.data[p]['attributes'][k])

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[4]}/{self.code}"
        d = Downlaoder(url)
        for k in list(d.data[0]['attributes'].keys()):
            setattr(self, k, d.data[0]['attributes'][k])

class LeiIssuers:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'issuers.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating countries.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[1]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        data = []
        for item in d.data:
            jurisdiction = get_jurisdiction(item)
            new_item = item
            new_item['attributes']['jurisdiction'] = jurisdiction
            data.append(new_item)
        self.data = data
        save(self.FILE, data)

class LeiIssuer:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        li = LeiIssuers()
        codes = [i['id'] for i in li.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached countries. Updating dataset.")
            li.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No country with the code {self.code}")
                return
        self.name = li.data[p]['attributes']['name']
        self.lei = li.data[p]['attributes']['lei']
        self.marketingName = li.data[p]['attributes']['marketingName']
        self.website = li.data[p]['attributes']['website']
        self.accreditatioDate = li.data[p]['attributes']['accreditationDate']
        self.jurisdiction = li.data[p]['attributes']['jurisdiction']
        #self.jurisdiction = self.get_jurisdiction(li.data[p])

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[1]}/{self.code}"
        d = Downlaoder(url)
        self.name = d.data[0]['attributes']['name']
        self.lei = li.data[0]['attributes']['lei']
        self.marketingName = li.data[0]['attributes']['marketingName']
        self.website = li.data[0]['attributes']['website']
        self.accreditatioDate = li.data[0]['attributes']['accreditatioDate']
        self.jurisdiction = get_jurisdiction(li.data[0])

def get_jurisdiction(data_point):
    try:
        id = data_point['id']
        relationships = list(data_point['relationships'].keys())
        if 'jurisdictions' in relationships:
            r = Downloader(f"{BASE_URL}/{L1_ENDPOINTS[1]}/{id}/{L3_ENDPOINTS[15]}")
            return r.data[0]['attributes']['countryCode']
        else:
            return ''
    except:
        return ''

class LegalForms:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'lforms.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating legal forms.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[7]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class LegalForm:
    def __init__(self, code):
        self.code = code
        self.name = ''
        self._populate()

    def __str__(self):
        return f"{'Entity Code:':<18}{self.code:<20}\n{'Entity name:':<18}{self.name:<20}\n{'Entity country:':<18}{self.country:<20}"

    def _populate(self):
        lf = LegalForms()
        codes = [i['attributes']['code'] for i in lf.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached legal forms. Updating dataset.")
            lf.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No legal form with the code {self.code}")
                return
        self.country = lf.data[p]['attributes']['country']
        names = [i for i in lf.data[p]['attributes']['names']]
        for name in names:
            if name['languageCode'] == 'en':
                self.name = name['localName']
                self.language = name['languageCode']
        if not self.name:
            self.name = lf.data[p]['attributes']['names'][0]['localName']
            self.language = lf.data[p]['attributes']['names'][0]['language']
        self.country_code = lf.data[p]['attributes']['countryCode']
        self.status = lf.data[p]['attributes']['status']
        self.jurisdiction = lf.data[p]['attributes']['jurisdiction']

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[7]}/{self.code}"
        d = Downloader(url)
        self.country = d.data[0]['attributes']['country']
        names = [i for i in d.data[0]['attributes']['names']]
        for name in names:
            if name['languageCode'] == 'en':
                self.name = name['localName']
                self.language = name['languageCode']
        if not self.name:
            self.name = names[0]['localName']
            self.language = names[0]['language']
        self.country_code = d.data[0]['attributes']['countryCode']
        self.status = d.data[0]['attributes']['status']
        self.jurisdiction = d.data[0]['attributes']['jurisdiction']

class Regions:
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'caches', 'regions.pkl')

    def __init__(self):
        self.data = []
        if not os.path.isfile(self.FILE):
            print("Updating regions.")
            self.update()
        else:
            self.data = load(self.FILE)

    def update(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[8]}"
        params = {
            'page[size]': 100,
            'page[number]': 1
        }
        d = Downloader(url, params=params)
        self.data = d.data
        save(self.FILE, d.data)

class Region:
    def __init__(self, code):
        self.code = code
        self._populate()

    def _populate(self):
        r = Regions()
        codes = [i['attributes']['code'] for i in r.data]
        try:
            p = codes.index(self.code)
        except ValueError:
            print(f"Code {self.code} not in the chached regions. Updating dataset.")
            r.update()
            try:
                p = codes.index(self.code)
            except:
                print(f"Error: No region with the code {self.code}")
                return
        name = r.data[p]['attributes']['name']
        if not name:
            self.name = 'Unspecified'
        else:
            self.name = name

    def download(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[8]}/{self.code}"
        d = Downlaoder(url)
        name = d.data[0]['attributes']['name']
        if not name:
            self.name = 'Unspecified'
        else:
            self.name = name

def get_region_name(region_code):
    r = Region(region_code)
    return r.name
