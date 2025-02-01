Feature: Orders Creation API Testing

  Scenario Outline: Test order creation with valid inputs
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   | note   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> | <note> |
    Then the response status should be "201"
    
    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note                |
      |        100 |       10 |    2025-02-10 |          25.50 |           0.1 | "Priority Delivery" |
      |        101 |       10 |    2025-02-10 |          25.50 |               |                     |

  Scenario Outline: Test order creation with missing required fields
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   | note   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> | <note> |
    Then the response status should be "<status_code>"
    And the response should have the "<error_message>"

    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note                | status_code | error_message                 |
      |            |       10 |    2025-02-10 |          25.50 |           0.1 | "Priority Delivery" |         400 | Missing field: product_id     |
      |        101 |          |    2025-02-10 |          25.50 |           0.1 | "Priority Delivery" |         400 | Missing field: quantity       |
      |        103 |       10 |               |          25.50 |           0.1 | "Priority Delivery" |         400 | Missing field: delivery_date  |
      |        103 |       10 |    2025-02-10 |                |           0.1 | "Priority Delivery" |         400 | Missing field: price_per_unit |

  Scenario Outline: Test order creation with unauthorised user
    Given I have a "<token_type>" user auth token
    When I send a request to create an order with the following data
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note                |
      |        101 |       10 |    2025-02-10 |           25.3 |           0.1 | "Priority Delivery" |
    Then the response status should be "<status_code>"

    Examples:
      | token_type | status_code |
      | invalid    |         401 |
      | missing    |         401 |
