from behave import given, when, then
from builders.order_builder import OrderBuilder
from api.orders_api import OrdersApi

@given('I am an authenticated user')
def step_given_authenticated_user(context):
    context.user = 'authenticated_user'

@when('I send a request to create an order with the following data')
def step_when_send_request(context):
    order_data = {}
    for row in context.table:
        order_data['product_id'] = row['product_id']
        order_data['quantity'] = row['quantity']
        order_data['delivery_date'] = row['delivery_date']
        order_data['price_per_unit'] = row['price_per_unit']
        order_data['discount_rate'] = row['discount_rate']
        
    order_create_request = OrderBuilder()\
        .with_product_id(order_data['product_id'])\
        .with_quantity(order_data['quantity'])\
        .with_delivery_date(order_data['delivery_date'])\
        .with_price_per_unit(order_data['price_per_unit'])\
        .with_discount_rate(order_data['discount_rate'])\
        .build()
    
    context.response = OrdersApi().create_order(order_create_request)
    
@then(u'the response status should be "{status_code}"')
def step_then_verify_status(context, status_code):
    assert context.response.status_code == int(status_code), \
        f"Expected {status_code}, but got {context.response.status_code}"