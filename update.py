#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:30:56 2020

@author: youssouf
"""

import pandas as pd
from os import path
from datetime import datetime

country_key = 'Country/Region'
lat_key = 'Lat'
long_key = 'Long'

data_path = path.join(path.dirname(path.abspath(__file__)),"data")

files = [
        "COVID19_CC_UPDATED.csv",
        "COVID19_DC_UPDATED.csv",
        "COVID19_RC_UPDATED.csv"
    ]



