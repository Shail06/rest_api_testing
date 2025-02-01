from api.base_api import BaseApi
import json

class OrdersApi(BaseApi):
    
    def __init__(self, auth_token=None):
        super().__init__()
        self.auth_token = auth_token
    
    def create_order(self, order_data):
        headers = {"Content-Type": "application/json"}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return self.post('/api/v1/orders/create', request_body=order_data, headers=headers)
