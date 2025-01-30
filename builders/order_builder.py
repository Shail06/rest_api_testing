
class OrderBuilder():
    
    def __init__(self):
        self.order_data = {
            "product_id": 123,
            "quantity": 5,
            "delivery_date": "2025-02-28",
            "price_per_unit": 10.50,
            "discount_rate": 0.15,
            "note": "Priority delivery"
        }
    
    def with_product_id(self, product_id):
        self.order_data['product_id'] = product_id
        return self
    
    def with_quantity(self, quantity):
        self.order_data['quantity'] = quantity
        return self
    
    def with_delivery_date(self, delivery_date):
        self.order_data['delivery_date'] = delivery_date
        return self
    
    def with_price_per_unit(self, price_per_unit):
        self.order_data['price_per_unit'] = price_per_unit
        return self
    
    def with_discount_rate(self, discount_rate):
        self.order_data['discount_rate'] = discount_rate
        return self
    
    def build(self):
        return self.order_data