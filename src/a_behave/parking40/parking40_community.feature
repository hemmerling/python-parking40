##
#
#  @package parking40
#  @file    parking40_community.feature
#  @author  Rolf Hemmerling
#  @date    2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  Menu item "Community"
#

Feature: Community

  As a car-driver
  I may contribute parking informations to the community
  So that the parking database is expanding and is up to date

  @PublishParkingPlaceOffer
  Scenario: publishParkingPlaceOffer
    Given I logged into the parking-app
    When I want to tell about a parking place
    Then I may pass my the position of the parking place to the parking-app

  @PublishParkingPlaceRestriction
  Scenario: publishParkingPlaceRestriction
    Given I logged into the parking-app
    When I want to tell about a parking restriction
    Then I may pass my the position of the parking restriction to the parking-app

  @PublishParkingPlaceByAuthority
  Scenario: publishParkingPlaceByAuthority
    Given I logged into the parking-app
    When I am an authority and want to tell about a parking scheduling
    Then I may pass my data to the parking-app

  @SendUrgendRemovalRequest
  Scenario: pushUrgendRemovalRequest
    Given I connected to the Internet by smartphone or by parking app
    When there is an need for urgend removal of a parked car
    Then I may pass a request to the online service

  @ReceiveUrgendRemovalRequest
  Scenario: pushUrgendRemovalRequest
    Given I connected to the Internet by smartphone or by parking app
    When there is an need for urgend removal of a parked car
    Then I may receive a request by the online service

