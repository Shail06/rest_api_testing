Feature: Orders Creation API Testing

  Scenario Outline: Order creation with different inputs
    Given I am an authenticated user
    When I send a request to create an order with the following data
      | product_id   | quantity   | delivery_date   | price_per_unit   | discount_rate   |
      | <product_id> | <quantity> | <delivery_date> | <price_per_unit> | <discount_rate> |
    Then the response status should be "<status_code>"

    Examples:
      | product_id | quantity | delivery_date | price_per_unit | discount_rate | status_code | error_message |
      |        123 |       10 |    2025-02-10 |          25.50 |           0.1 |         201 |               |
      |        124 |       10 |    2025-02-10 |          25.50 |           0.1 |         201 |               |
