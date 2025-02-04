# Test Approach & Strategy

This document outlines the test approach and strategy for the Order Creation API. The primary objective is to ensure the API behaves as expected in various scenarios, including functional, non-functional, and edge case testing. The document will detail the overall testing methodology, test types, scope, and the tools used.

### Test Scenarios

Following are the test scenarios:

#### Happy Paths / Positive Tests

| TestCase ID | Test Description                                                      | Expected Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TC-001      | Check if Order is created successfully                                | `201 Created` with correct order details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TC-002      | Check if Order is created successfully (with missing optional fields) | `201 Created` with correct order details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TC-003      | Check if API response has valid fields & values                       | `201 Created` with correct order details<br />`product_id` from response matches request<br />`quantity` from response matches request<br />`delivery_date` from response matches request<br />`price_per_unit` from response matches request<br />`discount_applied` from response matches request<br />`order_id` should be a UUID<br />`confirmation_code` should present and be a string<br />`total_amount` should be float and should be calculated as: `quantity x price_per_unit x(1-discount_rate)` |
| TC-004      | Check if multiple same requests create different order each time      | `201 Created` multiple times, `order_id` should be different                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

#### Negative Tests

| TestCase ID | Test Description                                                 | Expected Outcome                                   |
| ----------- | ---------------------------------------------------------------- | -------------------------------------------------- |
| TC-005      | Order creation with missing `product_id`                       | `400 Bad Request` with error message             |
| TC-006      | Order creation with missing `quantity`                         | `400 Bad Request` with error message7            |
| TC-007      | Order creation with missing `delivery_date`                    | `400 Bad Request` with error message             |
| TC-008      | Order creation with missing `price_per_unit`                   | `400 Bad Request` with error message             |
| TC-009      | Order creation with `product_id` as string (PRODUCT106)        | `400 Bad Request`, must be integer               |
| TC-010      | Order creation with `product_id` as -ve integer (-106)         | `400 Bad Request`, must be positive              |
| TC-011      | Order creation with `quantity` as 0                            | `400 Bad Request`, `quantity` must be `>= 1` |
| TC-012      | Order creation with `quantity` as -1                           | `400 Bad Request`, must be positive              |
| TC-013      | Order creation with `quantity` as decimal (10.23)              | `400 Bad Request`, must be integer               |
| TC-014      | Order creation with `quantity` as string (TWENTY)              | `400 Bad Request`, must be integer               |
| TC-015      | Order creation with wrong `delivery_date` format (2025-Feb-10) | `400 Bad Request`, must be `YYYY-MM-DD`        |
| TC-016      | Order creation with wrong `delivery_date` format (20/Feb/2025) | `400 Bad Request`, must be `YYYY-MM-DD`        |
| TC-017      | Order creation with `price_per_unit` as -99.99                 | `400 Bad Request`, must be positive              |
| TC-018      | Order creation with `price_per_unit` as 0                      | `400 Bad Request`, must be >=1                   |
| TC-019      | Order creation with `price_per_unit` as string (TEN)           | `400 Bad Request`, must be decimal               |
| TC-020      | Order creation with `discount_rate = 1.5` (Greater than 1)     | `400 Bad Request`, must be between `0-1`       |
| TC-021      | Order creation with `discount_rate = -1.5` (Less than 0)       | `400 Bad Request`, must be between `0-1`       |
| TC-022      | Order creation with `discount_rate = ZERO` (a string)          | `400 Bad Request`, must be a decimal             |

#### Non Functional Tests

| TestCase ID | Test Description                                           | Expected Outcome                            |
| ----------- | ---------------------------------------------------------- | ------------------------------------------- |
| TC-023      | Order creation with Invalid authentication token provided | `401 Unauthorized`                        |
| TC-024      | Order creation with No authentication token provided      | `401 Unauthorized`                        |
| TC-025      | Check if API responds within an acceptable time            | The response time should be less than 500ms |

### Tools & Frameworks

**Test Automation Framework** :

* **Python3:** Module *requests* for testing http methods
* **BDD** : Feature files written in Gherkin with **Behave** for behavior-driven testing.
* **Allure Reports** : For generating detailed test execution reports with intermediate request/response JSONs and assertions.

### Test Environment

The Tests can be executed on:

* Local Environment ( Dependencies: `behave`, `requests`, `allure`)
* Docker Container
