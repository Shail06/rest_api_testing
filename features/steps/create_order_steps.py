from behave import given, when, then
from builders.order_builder import OrderBuilder
from api.orders_api import OrdersApi
import allure
import json

@given('I have a "{token_type}" user auth token')
def step_given_authenticated_user(context, token_type):
    if token_type == "valid":
        context.auth_token = "c0c3zxfep9pjz7fe"
    elif token_type == "invalid":
        context.auth_token = "blah-blah"
    elif token_type == "missing":
        context.auth_token = ""
    allure.attach(context.auth_token, name="Auth Token", attachment_type=allure.attachment_type.TEXT)

@when('I send a request to create an order with the following data')
def step_when_send_request(context):
    request_payload={}
    for row in context.table:
        order_request = OrderBuilder()\
        .with_product_id(get_value(row['product_id'], int))\
        .with_quantity(get_value(row['quantity'], int))\
        .with_delivery_date(get_value(row['delivery_date'], str))\
        .with_price_per_unit(get_value(row['price_per_unit'], float))\
        .with_discount_rate(get_value(row['discount_rate'], float))\
        .with_note(get_value(row['note'], str))\
        .build()
        context.request = order_request
        context.response = OrdersApi(context.auth_token).create_order(order_request)
        request_payload = json.dumps(order_request, indent=2)
    allure.attach(request_payload, name="Request Payload", attachment_type=allure.attachment_type.JSON)

# def get_value(field_value, expected_type):
#     if field_value in [None, ""]:
#         return None
#     elif isinstance(field_value, expected_type):
#         return expected_type(field_value)
#     else:
#         return field_value
    
def get_value(value, expected_type):
    if value in [None, ""]:
        return None
    if isinstance(value, str):
        if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value

    if isinstance(value, expected_type):
        return value
    return value

@then('the response status should be "{status_code}"')
def step_then_verify_status(context, status_code):
    soft_assert = context.soft_assert
    allure.attach(context.response.text, name="Response Payload", attachment_type=allure.attachment_type.JSON)
    soft_assert.soft_assert(context.response.status_code == int(status_code), \
        f"Expected {status_code}, but got {context.response.status_code}")
    soft_assert.assert_all()
        
@then('the response should have the "{error_message}"')
def step_then_check_error_message(context, error_message):
    response_json = context.response.json()
    soft_assert = context.soft_assert
    soft_assert.soft_assert("error" in response_json, "Error message not found in response")
    if("error" in response_json):
        soft_assert.soft_assert(response_json["error"] == error_message, f"Expected {error_message}, but got {response_json}")
    soft_assert.assert_all()

@then('the response should have valid fields and values')
def step_then_validate_response(context):
    response_order = context.response.json()
    response_order_details = response_order["order_details"]
    request_order_details = context.request
    
    soft_assert = context.soft_assert
    
    soft_assert.soft_assert(response_order_details["product_id"] == request_order_details["product_id"], f'product_id mismatch! \nExpected: {request_order_details["product_id"]}, Actual: {response_order_details["product_id"]}')
    soft_assert.soft_assert(response_order_details["quantity"] == request_order_details["quantity"], f'quantity mismatch! \nExpected: {request_order_details["quantity"]}, Actual: {response_order_details["quantity"]}')
    soft_assert.soft_assert(response_order_details["delivery_date"] == request_order_details["delivery_date"], f'delivery_date mismatch! \nExpected: {request_order_details["delivery_date"]}, Actual: {response_order_details["delivery_date"]}')
    soft_assert.soft_assert(response_order_details["price_per_unit"] == request_order_details["price_per_unit"], f'price_per_unit mismatch! \nExpected: {request_order_details["price_per_unit"]}, Actual: {response_order_details["price_per_unit"]}')
    soft_assert.soft_assert(response_order_details["discount_applied"] == request_order_details["discount_rate"], f'discount_rate mismatch! \nExpected: {request_order_details["discount_rate"]}, Actual: {response_order_details["discount_applied"]}')
    soft_assert.assert_valid_uuid(response_order_details["order_id"], "Invalid order_id format")
    soft_assert.soft_assert(isinstance(response_order_details["confirmation_code"], str), "Invalid confirmation_code type")
    soft_assert.soft_assert(isinstance(response_order_details["total_amount"], float), "Invalid total_amount type")
    soft_assert.assert_all()
    