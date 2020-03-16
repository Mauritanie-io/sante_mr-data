#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:19:15 2020

@author: youssouf
"""

import pycountry

country_key = "Country/Region"
lat_key = 'Lat'
long_key = 'Long'

def get_country(value):
    value = value.strip()
    if value == "Vietnam":
        value = 'Viet Nam'
    if value == 'UK':
        value = 'GB'
    if value == 'Diamond Princess':
        value = 'JPN'
    if value == 'Iran':
        value = 'IRN'
    if value == 'S. Korea' or value == 'Korea, South':
        value = 'KOR'
    if value == 'Russia':
        value = 'RUS'
    if value == 'Brunei':
        value = 'BRN'
    if value == 'Palestine':
        value = 'PSE'
    if value == 'Moldova':
        value = 'MDA'
    if value == 'Bolivia':
        value = 'BOL'
    if value == 'Venezuela':
        value = 'VEN'
    if value == 'Ivory Coast':
        value = 'CIV'
    if value == 'Taiwan*' or value == 'Taiwan':
        value = 'TWN'
    if value == 'DRC':
        value = 'COD'
    if value == 'Vatican City':
        value = 'VAT'
    if value == 'St. Barth':
        value = 'BLM'
    if value == 'St. Vincent Grenadines':
        value = 'VCT'
    if value == 'U.S. Virgin Islands':
        value = 'VIR'
    if value == 'Saint Martin':
        value = 'MAF'
    if value == 'CAR':
        value = 'CAF'
    if value == 'UAE':
        value = 'ARE'
    for country in pycountry.countries:
        if country.name in value or country.alpha_2 == value or country.alpha_3 == value:
            return country.name
    return value