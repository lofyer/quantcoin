import requests
from time import time
import json

class binanceApi():
    def __init__(self, api_key, secret_key, endpoint):
        self.api_key = api_key
        self.secret_key = secret_key
        self.endpoint = endpoint

    def systemStatus(self):
        requestUrl = self.endpoint + '/wapi/v3/systemStatus.html'
        try:
            time_before = time()
            r = requests.get(requestUrl, timeout=1)
            time_after = time()
            time_taken = time_after-time_before
            if r.status_code == 200:
                j = json.loads(r.text)
                return (j['status'], time_taken)
        except Exception as e:
            return (1, 0)