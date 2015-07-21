##
#
#  @package parking40
#  @file    parking40_want-to-park.feature
#  @author  Rolf Hemmerling
#  @date    2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  Menu item "Car Operation / I want to park"
#  Menu item "Car Operation / I park"
#

Feature: Car driver wants to park

  As a car-driver driving a car
  I want find a parking-place
  So that I can park

  @WantToPark
  Scenario: The driver want to park the car
    Given I am driving the car
    When I want to park
    Then I am offered free parking-places

  @SelectParkingplace
  Scenario: The driver selects a parking-place
    Given I am driving the car
    When I found free parking-places
    Then I select a parking-place

  @Parking
  Scenario: The driver parks the car
    Given I am driving the car
    When I selected a parking-place
    Then I park the car

