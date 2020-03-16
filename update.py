#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:30:56 2020

@author: youssouf
"""

import pandas as pd
from os import path, listdir
from countries import country_key, lat_key, long_key
import shutil

def add_country(df, country, latitude=None, longitude=None):
    data = {}
    data[country_key] = country
    data[lat_key] = latitude
    data[long_key] = longitude
    for col in df.columns[3:]:
        data[col] = 0
    return df.append(data, ignore_index = True)

def update_countries(df, data_path, files):
    countries = df[country_key].values
    for f in files:
        dff = pd.read_csv(path.join(data_path, f), sep=",")
        
        for country in countries:
            if country == 'Total:':
                continue
            if country not in dff[country_key].values:
                dff = add_country(dff, country)
        dff.to_csv(path.join(data_path, f), header=True, index=False)

def parse_value(value):
    value = str(value).strip()
    if value == '':
        return 0
    return int(value.replace(',', ''))

def add_value(df, date, country, value, last_value):
    for index in df.index:
        if df[country_key][index] == country:
            value = parse_value(value)
            if last_value > value:
                value = last_value
            df.at[index, date] = value 
    return df

def update_field(date, df, data_path, updated_file, field):
    dff = pd.read_csv(path.join(data_path, updated_file), sep=",")
    last_date = dff.columns.values[len(dff.columns) -1]
    column = df[[country_key, field]]
    dff.insert(len(dff.columns), date, 0)
    for index in column.index:
        dff = add_value(dff, date, column[country_key][index], column[field][index], dff[last_date][index])
        dff.to_csv(path.join(data_path, updated_file), header=True, index=False)

def update_date(f, df, data_path, updated_files, fields):
    col = f.split('.')[0]
    date = col.replace('-','/')
    for uf, field in zip(updated_files, fields):
        update_field(date, df, data_path, uf, field)
        
def archive_file(f, data_path, archived_path):
    source = path.join(daily_path, f)
    destination = archived_path
    shutil.move(source, destination)
    
data_path = path.join(path.dirname(path.abspath(__file__)), "data")
daily_path = path.join(data_path, "daily")
archived_path = path.join(data_path, "archived")
        
if __name__ == "__main__":
    files = [f for f in listdir(daily_path) if path.isfile(path.join(daily_path, f))]
    files.sort()
    updated_files = [
        "COVID19_CC_UPDATED.csv",
        "COVID19_DC_UPDATED.csv",
        "COVID19_RC_UPDATED.csv"
    ]
    fields = ['TotalCases',
              'TotalDeaths',
              'TotalRecovered']
    for f in files:
        df = pd.read_csv(path.join(daily_path, f), sep=",")
        update_countries(df, data_path, updated_files)
        update_date(f, df, data_path, updated_files, fields)
        archive_file(f, daily_path, archived_path)