import os
from gleif.downloader import Downloader
from gleif.objects import RegistrationAuthority
from gleif.objects import Jurisdiction
from gleif.objects import Country
from gleif.objects import LegalForm
from gleif.utils import load, save
from gleif import BASE_URL, L1_ENDPOINTS, L3_LEI_RECORDS

class Record:
    def __init__(self, lei):
        self.lei = lei
        self._populate()
        self.attributes = [item for item in dir(self) if not item.startswith('_')]

    #def __str__(self):
    #    pass

    def _populate(self):
        url = f"{BASE_URL}/{L1_ENDPOINTS[0]}/{self.lei}"
        record = Downloader(url)
        entity = self._format_record(record.data[0]['attributes']['entity'])
        [setattr(self, attribute, entity[attribute]) for attribute in entity.keys()]
        relationships = [key for key in record.data[0]['relationships'].keys()
            if key in L3_LEI_RECORDS]
        for relationship in relationships:
            setattr(self, relationship.replace('-', '_'),
                record.data[0]['relationships'][relationship])

    def __getattribute__(self, attribute):
        if attribute.replace('_', '-') in L3_LEI_RECORDS:
            if attribute in self.__dict__:
                try:
                    try:
                        url = self.__dict__[attribute]['links']['related']
                    except:
                        url = self.__dict__[attribute]['links']['lei-record']
                    return self._target(Downloader(url))
                except:
                    return None
            else:
                return None
        else:
            return super(Record, self).__getattribute__(attribute)

    def _target(self, d_object):
        if d_object.paginated:
            if d_object.data[0]['type'] == 'isins':
                return [item['attributes']['isin'] for item in d_object.data]
            elif d_object.data[0]['type'] == 'lei-records':
                for item in d_object.data:
                    item['attributes']['entity']['lei'] = item['id']
                return [self._format_record(item['attributes']['entity']) for
                    item in d_object.data]
        else:
            if d_object.data[0]['type'] == 'lei-records':
                d_object.data[0]['attributes']['entity']['lei'] = d_object.data[0]['id']
                return self._format_record(d_object.data[0]['attributes']['entity'])
            elif d_object.data[0]['type'] == 'lei-issuers':
                return d_object.data[0]['attributes']

    def _format_record(self, entity_record):
        entity_record['jurisdiction'] = Jurisdiction(entity_record['jurisdiction']).name
        entity_record['headquartersAddress']['addressLines'] = \
            ' '.join(entity_record['headquartersAddress']['addressLines'])
        entity_record['headquartersAddress']['country'] = \
            Country(entity_record['headquartersAddress']['country']).name
        entity_record['legalAddress']['addressLines'] = \
            ' '.join(entity_record['legalAddress']['addressLines'])
        entity_record['legalAddress']['country'] = \
            Country(entity_record['legalAddress']['country']).name
        entity_record['legalForm'] = LegalForm(entity_record['legalForm']['id']).name
        entity_record['legalName'] = entity_record['legalName']['name']
        entity_record['registeredAt'] = RegistrationAuthority(entity_record['registeredAt']['id']).internationalName
        entity_record['successorEntity'] = entity_record['successorEntity']['lei']
        return entity_record


class Entity:
    def __init__(self, lei):
        self.lei = lei
        url = f"{BASE_URL}/{L1_ENDPOINTS[0]}/{self.lei}"
        d = Downloader(url)
        self.record = d.data[0]['attributes']['entity']
