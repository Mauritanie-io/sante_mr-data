#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:30:56 2020

@author: youssouf
"""

import pandas as pd
from os import path, listdir
from datetime import datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="sante_mr")

country_key = 'Country/Region'
lat_key = 'Lat'
long_key = 'Long'

data_path = path.join(path.dirname(path.abspath(__file__)), "data")
daily_path = path.join(data_path, "daily")

def update_countries(df, directory, files):
    countries = df[country_key]
    locations = [geolocator.geocode(country) for country in countries]
    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    for f in files:
        dff = pd.read_csv(path.join(directory, f), sep=",")
        
        
if __name__ == "__main__":
    files = [f for f in listdir(daily_path) if path.isfile(path.join(daily_path, f))]
    updates_files = [
        "COVID19_CC_UPDATED (copy).csv",
        "COVID19_DC_UPDATED (copy).csv",
        "COVID19_RC_UPDATED (copy).csv"
    ]
    for f in files:
        df = pd.read_csv(path.join(daily_path, f), sep=",")
        update_allcountries(daily_path, f, data_path, updates_files)

