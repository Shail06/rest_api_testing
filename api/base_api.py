import requests

class BaseApi:
    BASE_URL = "https://ku3d2-ncth-347x-dot-neptune-cicd.ew.r.appspot.com";
    
    def post(self, endpoint, request_body=None, headers=None):
        response = requests.post(self.BASE_URL + endpoint, json=request_body, headers=headers)
        return response