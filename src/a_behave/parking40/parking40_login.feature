##
#
#  @package parking40
#  @file    parking40_login.feature
#  @author  Rolf Hemmerling
#  @date    2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  Menu item "User / Login"
#

Feature: Login

  As a car-driver
  I want to login at the parking-app
  So that use it

  @Login
  Scenario: login
    Given I activated the parking-app
    When I execute the function user/login
    Then I may pass my username and password to the parking-app

