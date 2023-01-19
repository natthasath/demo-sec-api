from decouple import config
from fastapi.responses import JSONResponse
from ratelimit import *
import requests
import json

class SecService:
    def __init__(self):
        self.env = ''

    @rate_limited(1500, 300)

    def config(self, fund_factsheet):
        content = {"message": True}
        response = JSONResponse(content=content)
        response.set_cookie(key='fund_factsheet', value=fund_factsheet)
        return response

    def get_fund_amc(self, key, url):
        headers = {
            'Ocp-Apim-Subscription-Key': key
        }
        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 401:
            return JSONResponse(status_code=401, content={"message": "Invalid subscription key"})
        elif response.status_code == 404:
            return JSONResponse(status_code=404, content={"message": "Resource not found"})

    def get_fund_search(self, key, url, name):
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/json'
        }
        data = {
            "name": name
        }
        response = requests.post(url, data=json.dumps(data), headers = headers)

        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 401:
            return JSONResponse(status_code=401, content={"message": "Invalid subscription key"})
        elif response.status_code == 404:
            return JSONResponse(status_code=404, content={"message": "Resource not found"})