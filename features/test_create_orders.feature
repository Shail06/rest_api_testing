Feature: Orders Creation API Testing

  Scenario Outline: (Happy Path) Check if Order is created successfully
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   | note   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> | <note> |
    Then the response status should be "201"

    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note              |
      |        100 |       10 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |
      |        101 |       10 |    2025-02-10 |          25.50 |               |                   |

  Scenario: (Happy Path) Check if API response has valid fields & values
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note              |
      |        102 |       10 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |
    Then the response status should be "201"
    And the response should have valid fields and values

  Scenario: (Happy Path) Check if multiple same requests create different order each time
    Given I have a "valid" user auth token
    When I send 2 requests to creating an order
    Then the responses should have different "order_id"

  Scenario Outline: (Negative Tests) Order creation with missing required fields
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   | note   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> | <note> |
    Then the response status should be "<status_code>"
    And the response should have the "<error_message>"

    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note              | status_code | error_message                 |
      |            |       10 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Missing field: product_id     |
      |        103 |          |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Missing field: quantity       |
      |        104 |       10 |               |          25.50 |           0.1 | Priority Delivery |         400 | Missing field: delivery_date  |
      |        105 |       10 |    2025-02-10 |                |           0.1 | Priority Delivery |         400 | Missing field: price_per_unit |

  Scenario Outline: (Negative Tests) Order creation with invalid field values
    Given I have a "valid" user auth token
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   | note   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> | <note> |
    Then the response status should be "<status_code>"
    And the response should have the "<error_message>"

    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note              | status_code | error_message                                |
      | PRODUCT106 |       10 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid product_id: must be an integer       |
      |       -106 |       10 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid product_id: must be positive integer |
      |        107 |        0 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid quantity: must be >= 1               |
      |        108 |       -1 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid quantity: must be >= 1               |
      |        109 |    10.23 |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid quantity: must be an integer         |
      |        110 | TWENTY   |    2025-02-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid quantity: must be a number           |
      |        111 |       10 |   2025-Feb-10 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid date format. Use YYYY-MM-DD format   |
      |        112 |       10 |   20/Feb/2025 |          25.50 |           0.1 | Priority Delivery |         400 | Invalid date format. Use YYYY-MM-DD format   |
      |        113 |       10 |    2025-02-10 |         -99.99 |           0.1 | Priority Delivery |         400 | price_per_unit cannot be negative            |
      |        114 |       10 |    2025-02-10 |              0 |           0.1 | Priority Delivery |         400 | price_per_unit must be >=0.01                |
      |        115 |       10 |    2025-02-10 | TEN            |           0.1 | Priority Delivery |         400 | Invalid price_per_unit: must be a number     |
      |        116 |       10 |    2025-02-10 |          25.50 |           1.5 | Priority Delivery |         400 | discount_rate must be <=1                    |
      |        117 |       10 |    2025-02-10 |          25.50 |          -1.5 | Priority Delivery |         400 | discount_rate must be >=0                    |
      |        118 |       10 |    2025-02-10 |          25.50 | ZERO          | Priority Delivery |         400 | discount_rate must be >=0                    |

  Scenario Outline: (Security Tests) Order creation with unauthorised user
    Given I have a "<token_type>" user auth token
    When I send a request to create an order with the following data
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | note              |
      |        101 |       10 |    2025-02-10 |           25.3 |           0.1 | Priority Delivery |
    Then the response status should be "<status_code>"

    Examples:
      | token_type | status_code |
      | invalid    |         401 |
      | missing    |         401 |
