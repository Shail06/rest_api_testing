from api.base_api import BaseApi

class OrdersApi(BaseApi):
    
    def create_order(self, order_data):
        return self.post('/api/v1/orders/create', order_data)
