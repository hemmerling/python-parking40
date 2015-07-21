#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      mockup.py
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

class Mockup(object):
    """
    @class   Parking40
    @brief   Parking40 business logic
    """

    def __init__(self):
        """
        @fn      __init__
        @brief   Constructor
        """
        self.username = "Rolf"
        self.password = "codefest8"
        self.position = [52.274748699999996, 10.529506699999999]
        self.freeParkingplace1 = [52.274748699999996, 10.529506699999999]
        self.freeParkingplace2 = [52.274748699999996, 10.529506699999999]
        # Latitude, Longitude of Braunschweig, Pockelsstraße 11
        pass

    def login(self, username, password):
        """
        @fn      login
        @param   username
        @param   password
        @brief   Login
        """
        result = (username == self.username)&(password==self.password)
        return result

    def call_login(self):
        """
        @fn      login
        @brief   Call login of GUI
        """
        print "username =", self.username
        print "password =", self.password
        return self.username, self.password

    def getPosition(self):
        """
        @fn      getPosition
        @brief   Get the current position of the car
        """
        result = self.position
        print "position =", result
        return result

    def getFreeParkingPlaces(self, position):
        """
        @fn      getFreeParkingPlaces
        @param   position
        @brief   Get a list of free parking-placed by the online service
        """
        result = [self.freeParkingplace1,self.freeParkingplace2]
        return result

    def showFreeParkingPlaces(self, parkingPlaces):
        """
        @fn      showFreeParkingPlaces
        @param   parkingPlaces
        @brief   Show a list of free parking-places
        """
        print "Free parking places found ="
        for ii in parkingPlaces:
            print ii
        result = len(parkingPlaces)>0
        return result

    def call_selectParkingPlace(self, parkingPlaces):
        """
        @fn      call_selectParkingPlace
        @param   parkingPlaces
        @brief   Call login of GUI
        """
        parkingPlace = self.freeParkingplace1
        print "Free parking places found ="
        for ii in parkingPlaces:
            print ii
        print "Free parking place selected =",parkingPlace
        return parkingPlace



