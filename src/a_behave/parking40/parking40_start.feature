##
#
#  @package parking40
#  @file    parking40_start.feature
#  @author  Rolf Hemmerling
#  @date    2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  Menu item "Car Operation / I start the car"
#

Feature: Car is started by the driver

  As a car-driver
  I want to start the car
  So that I can drive

  @StartCar
  Scenario: start car
    Given I am not driving the car
    When I start driving
    Then my parking-place is set as free

