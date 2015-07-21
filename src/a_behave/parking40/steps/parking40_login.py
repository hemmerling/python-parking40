#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      parking40_login.py
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

@given(u'I activated the parking-app')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @given
    """
    assert True

@when(u'I execute the function user/login')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @when
    """
    parking40 = Parking40()
    mockup = Mockup()
    context.mockup = mockup
    context.parking40 = parking40
    assert True

@then(u'I may pass my username and password to the parking-app')
def step_impl(context):
    """
    @fn      step_impl
    @brief   @then
    """
    input = context.mockup.call_login()
    result =  context.parking40.login(input[0], input[1])
    assert result
