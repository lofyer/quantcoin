import requests
import json

class binanceApi():
    def __init__(self, api_key, secret_key, endpoint):
        self.api_key = api_key
        self.secret_key = secret_key
        self.endpoint = endpoint

    def endpointLatency(self):
        return 1

    def systemStatus(self):
        requestUrl = self.endpoint + '/wapi/v3/systemStatus.html'
        r = requests.get(requestUrl, timeout=1)
        if r.status_code != 200:
            return False
        j = json.loads(r.text)
        return (j['status'])
        #self.sessionId = j["inventory"]["uuid"]
        #print("Session: ", self.sessionId)