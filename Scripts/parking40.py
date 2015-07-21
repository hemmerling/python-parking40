#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      parking40-script.py
#  @brief     Python application "Parking 4.0"
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-03-08
#  @copyright Apache License, Version 2.0
#
#  parking40 - Python application "Parking 4.0"
#
#  Copyright 2015 Rolf Hemmerling
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
import os
from os import chdir
try:
    import parking40
except ImportError:
    os.chdir("./..")
    import parking40
from sys import argv

def main(argv_parameters):
    """
    @fn       main
    @brief    Execute the software
    """
    parking40.main(argv_parameters)
    return

if __name__ == '__main__':
    """
    @fn       __main___
    @brief    Execute the software
    """
    main(argv)
