from gleif.downloader import Downloader
from gleif import BASE_URL, L1_ENDPOINTS

def fuzzysearch(search_phrase):
    url = f"{BASE_URL}/{L1_ENDPOINTS[2]}"
    param_values = ['entity.legalName', 'fulltext', 'owns', 'ownedBy']
    params = {
        'field': f"{param_values[1]}",
        'q': f"{search_phrase}",
    }
    r = Downloader(url, params=params)

    dataset = []
    for i in r.data[0]:
        try:
            dataset.append((i['attributes']['value'],
                i['relationships']['lei-records']['data']['id']))
        except:
            dataset.append((i['attributes']['value'],''))
    return dataset

def autocomplete(search_phrase):
    url = f"{BASE_URL}/{L1_ENDPOINTS[3]}"
    param_values = ['fulltext', 'owns', 'ownedBy']
    params = {
        'field': f"{param_values[0]}",
        'q': f"{search_phrase}"
    }

    r = Downloader(url, params = params)
    dataset = []
    for i in r.data[0]:
        try:
            dataset.append((i['attributes']['value'],
                i['relationships']['lei-records']['data']['id']))
        except:
            dataset.append((i['attributes']['value'], ''))
    return dataset
