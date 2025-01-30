import requests

class BaseApi:
    BASE_URL = "";
    
    def post(self, endpoint, request_body=None, headers=None):
        response = requests.post(self.BASE_URL + endpoint, json=request_body, headers=headers)
        return response