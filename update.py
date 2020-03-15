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
    print(countries)
    locations = [geolocator.geocode(country) for country in countries]
    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    for f in files:
        dff = pd.read_csv(path.join(directory, f), sep=",")
        for country, latitude, longitude in zip(countries, latitudes, longitudes):
            if not country in dff[country_key]:
                data = [country] + [latitude] + [longitude] + [0]*len(dff.columns[3:])
                dff = dff.append(pd.DataFrame(data = data, columns = dff.columns))
        dff.to_csv(f, header=True, index=False)
        
        
if __name__ == "__main__":
    files = [f for f in listdir(daily_path) if path.isfile(path.join(daily_path, f))]
    updates_files = [
        "COVID19_CC_UPDATED (copy).csv",
        "COVID19_DC_UPDATED (copy).csv",
        "COVID19_RC_UPDATED (copy).csv"
    ]
    fields = {'total_cases': 'TotalCases',
    'total_deaths' : 'TotalDeaths',
    'total_recovered' : 'TotalRecovered'}
    for f in files:
        df = pd.read_csv(path.join(daily_path, f), sep=",")
        update_countries(df, data_path, updates_files)
        # update_date(f, df, data_path, updates_files, fields)

