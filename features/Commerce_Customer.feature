

Feature:  Commerce customer handling

  Background:
    Given User login to "https://admin-demo.nopcommerce.com/login" webpage

@smoke
  Scenario Outline: Create new customer record
    When user enters email as "<User>" and password a "<Pass>"
    When Customer submenu selected
    And Add new button clicked
    When All Customer details entered
    Then customer record created successfully
    Examples:
      | Pass  | User                |
      | admin | admin@yourstore.com |
      | admin | admin@yourstore.com |




  @sanity
  Scenario Outline: Create new customer record
    When user enters email as "<User>" and password a "<Pass>"
    When Customer submenu selected
    And Add new button clicked
    When All Customer details entered
    Then customer record created successfully
    Examples:
      | Pass   | User                |
      | admin  | admin@yourstore.com |
      | admin1 | admin@yourstore.com |