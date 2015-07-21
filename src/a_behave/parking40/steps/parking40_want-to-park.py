#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      parking40_want-to-park.py
#  @brief     Python application "Parking 4.0"
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  parking40 - Python application "Parking 4.0"
#
#  Copyright 2015 Rolf Hemmerling
#
#  Licensed under the GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""

from parking40 import Parking40
from mockup import Mockup

@given(u'I am driving the car')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @given
    """
    parking40 = Parking40()
    mockup = Mockup()
    context.mockup = mockup
    context.parking40 = parking40
    freeParkingPlaces = context.parking40.getFreeParkingPlaces()
    context.freeParkingPlaces = freeParkingPlaces
    context.parking40.isParking(False)
    assert True

@when(u'I want to park')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @when
    """
    result = context.parking40.wantToPark()
    assert result

@then(u'I am offered free parking-places')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @then
    """
    parkingPlaces = context.parking40.getFreeParkingPlaces()
    result = context.mockup.showFreeParkingPlaces(parkingPlaces)
    assert result

@when(u'I found free parking-places')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @when
    """
    parkingPlaces = context.parking40.getFreeParkingPlaces()
    result = context.mockup.showFreeParkingPlaces(parkingPlaces)
    context.parkingPlaces = parkingPlaces
    result = result | len(parkingPlaces)>0
    assert result

@then(u'I select a parking-place')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @then
    """
    parkingPlace = context.mockup.call_selectParkingPlace(\
                   context.parkingPlaces)
    result = context.parking40.selectParkingPlace(parkingPlace)
    assert result

@when(u'I selected a parking-place')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @when
    """
    parkingPlaces = context.parking40.getFreeParkingPlaces()
    parkingPlace = context.mockup.call_selectParkingPlace(\
                   parkingPlaces)
    result = context.parking40.selectParkingPlace(parkingPlace)
    assert result

@then(u'I park the car')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @then
    """
    context.parking40.isParking(True)
    result = context.parking40.parkTheCar()
    assert result
