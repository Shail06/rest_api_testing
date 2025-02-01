from behave import given, when, then
from builders.order_builder import OrderBuilder
from api.orders_api import OrdersApi

@given('I have a "{token_type}" user auth token')
def step_given_authenticated_user(context, token_type):
    if token_type == "valid":
        context.auth_token = "c0c3zxfep9pjz7fe"
    elif token_type == "invalid":
        context.auth_token = "47917491sgqhkj"
    elif token_type == "missing":
        context.auth_token = None

@when('I send a request to create an order with the following data')
def step_when_send_request(context):
    for row in context.table:
        order_request = OrderBuilder()\
        .with_product_id(int(row['product_id']) if row['product_id'] else None)\
        .with_quantity(row['quantity'] if row['quantity'] else None)\
        .with_delivery_date(row['delivery_date'] if row['delivery_date'] else None)\
        .with_price_per_unit(row['price_per_unit'] if row['price_per_unit'] else None)\
        .with_discount_rate(row['discount_rate'] if row['discount_rate'] else None)\
        .with_note(row['note']if row['note'] else None)\
        .build()
        context.response = OrdersApi(context.auth_token).create_order(order_request)

@then('the response status should be "{status_code}"')
def step_then_verify_status(context, status_code):
    assert context.response.status_code == int(status_code), \
        f"Expected {status_code}, but got {context.response.status_code}"
        
@then('the response should have the "{error_message}"')
def step_then_check_error_message(context, error_message):
    response_json = context.response.json()
    assert "error" in response_json, "Error message not found in response"
    assert response_json["error"] == error_message, f"Expected {error_message}, but got {response_json}"
