
class OrderBuilder():
    
    def __init__(self):
        self.order_data = {}
    
    def with_product_id(self, product_id):
        if product_id is not None:
            self.order_data['product_id'] = product_id
        return self
    
    def with_quantity(self, quantity):
        if quantity is not None:
            self.order_data['quantity'] = quantity
        return self
    
    def with_delivery_date(self, delivery_date):
        if delivery_date is not None:
            self.order_data['delivery_date'] = delivery_date
        return self
    
    def with_price_per_unit(self, price_per_unit):
        if price_per_unit is not None:
            self.order_data['price_per_unit'] = price_per_unit
        return self
    
    def with_discount_rate(self, discount_rate):
        if discount_rate is not None:
            self.order_data['discount_rate'] = discount_rate
        return self
    
    def with_note(self, note):
        if note is not None:
            self.order_data['note'] = note
        return self
    
    def build(self):
        return self.order_data