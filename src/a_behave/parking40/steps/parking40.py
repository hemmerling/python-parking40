#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      parking40.py
#  @brief     Python application "Parking 4.0"
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  parking40 - "Python application "Parking 4.0"
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
"""

from mockup import Mockup

class Parking40(object):
    """
    @class   Parking40
    @brief   Parking40 business logic
    """

    def __init__(self):
        """
        @fn      __init__
        @brief   Constructor
        """
        self.mockup = Mockup()
        self.status = False
        pass

    def isParking(self, status):
        """
        @fn      isParking
        @brief   Is-Parking called by GUI
        """
        self.status = status
        return True

    def login(self, username, password):
        """
        @fn      login
        @brief   Login called by GUI
        """
        result = self.mockup.login(username, password)
        return result

    def reportFreeParkingplace(self, position):
        """
        @fn      reportFreeParkingplace
        @brief   Report a free parking-place to the online service
        """
        result = self.mockup.reportFreeParkingplace(position)
        return result

    def startCar(self):
        """
        @fn      startCar
        @brief   The driver starts the car
        """
        position = self.mockup.getPosition()
        result = self.mockup.reportFreeParkingPlace(position)
        return result

    def wantToPark(self):
        """
        @fn      wantToPark
        @brief   Want-to-Park called by GUI
        """
        return True

    def getFreeParkingPlaces(self):
        """
        @fn      getFreeParkingPlaces
        @brief   Get-free-Parking-places called by GUI
        """
        position = self.mockup.getPosition()
        parkingPlaces = self.mockup.getFreeParkingPlaces(position)
        return parkingPlaces

    def selectParkingPlace(self, parkingPlace):
        """
        @fn      selectParkingPlace
        @param   parkingPlace
        @brief   Get-free-Parking-places called by GUI
        """
        position = self.mockup.getPosition()
        parkingPlaces = self.mockup.getFreeParkingPlaces(position)
        return parkingPlace

    def parkTheCar(self):
        """
        @fn      parkTheCar
        @brief   Park-the-Car called by GUI
        """
        return True
