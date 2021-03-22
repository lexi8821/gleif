import requests
from urllib import parse
from simplejson.errors import JSONDecodeError
import time, datetime

class Downloader:
    def __init__(self, url, params=None):
        self.url = url
        self.params = params
        self.sess = requests.Session()
        self.paginated = False
        self.response = dict()
        self.data = list()
        self.download()

    def __del__(self):
        if hasattr(self, 'sess'):
            self.sess.close()

    def download_page(self, url, params):
        r = self.sess.get(url, params=params)
        if r.status_code == 200:
            try:
                self.response = r.json()
            except JSONDecodeError:
                print("Error: Problem with the response format! Check url parameter.")
                self.response = ''
        elif r.status_code == 429:
            print(f"Too many requests response from the server. Throttling my requests at {datetime.datetime.now()}")
            time.sleep(15)
            self.download_page(url, params)
        else:
            print(f"Warning: Status code: {r.status_code} for {r.url}!")
            self.response = ''

    def download(self):
        if not self.response:
            self.download_page(self.url, self.params)
            self.pagination_test(self.response)
            self.load_data()
        if self.paginated:
            while len(self.data) < self.total:
                params = {
                    'page[size]' : self.perPage,
                    'page[number]': self.currentPage + 1
                }
                self.download_page(self.url, params = params)
                self.pagination_test(self.response)
                self.load_data()

    def load_data(self):
        if self.response and self.paginated:
            for i in self.response['data']:
                self.data.append(i)
        else:
            self.data.append(self.response['data'])

    def pagination_test(self, response):
        try:
            pagination = response['meta']['pagination']
            self.paginated = True
            self.currentPage = response['meta']['pagination']['currentPage']
            self.lastPage = response['meta']['pagination']['lastPage']
            self.total = response['meta']['pagination']['total']
            self.perPage = response['meta']['pagination']['perPage']
        except KeyError:
            self.paginated = False

if __name__ == '__main__':
    url = 'https://api.gleif.org/api/v1'
    lei = 'IYKCAVNFR8QGF00HV840'
    full_url = f"{url}/lei-records/{lei}/ultimate-parent"
    #full_url = f"{url}/entity-legal-forms/D8XQ"
    #full_url = f"{url}/fields"
    #params = {
    #    'page[size]': 100,
    #    'page[number]': 1
    #}

    downloader = Downloader(full_url)
    #r = requests.get('https://api.gleif.org/api/v1/lei-issuers/029200067A7K6CH0H586/jurisdictions')
    #j = r.json()
