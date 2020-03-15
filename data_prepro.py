#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:06:15 2020

@author: stef, youssouf
"""

import pandas as pd
from os import path

FIELDS = {'country': 'Country/Region',
    'total_cases': 'TotalCases',
    'total_deaths' : 'TotalDeaths',
    'total_recovered' : 'TotalRecovered'}

data_path = path.join(path.dirname(path.abspath(__file__)),"data")

def agg_data_bycountry(data_path, data_file):
    df = pd.read_csv(path.join(data_path, data_file), sep=",") 
    # Aggregate data per country
    df = df.groupby('Country/Region')
    agg_df = df.sum().reset_index()
    return agg_df

def add_local_data(data_path, full_data, new_data):    
    df = pd.read_csv(path.join(data_path, new_data), sep=",") 
    
def get_updates_country(country, df, key = 'total_cases'):
    # returns updates deaths, new cases and recovered from new dataframe per country
    print(country)
    x = df.loc[df['Country,\nOther'] == country, FIELDS[key]]  
    #print('-x :', x)
    if len(x.values) >0 :
        if clean_int(x.values[0]) is not None:
            return int(clean_int(x.values[0]))
        else :
            return None
    else :
        return None


def update_full_data(data_path, full_data, new_data, key = 'total_cases'):
    df_0 = pd.read_csv(path.join(data_path, full_data), sep=",")
    df = pd.read_csv(path.join(data_path, new_data), sep=",")
    
    for country in df_0['Country/Region']:
        df_0.iloc[:,-1][df_0['Country/Region']==country] = get_updates_country(country, df, key)      
    
    #[update_daily_data_country(df_0, df, country, key) for country in df_0['Country/Region']]
    
    #save data 
    file_name = full_data.split('.')[0]+'-'+ date.today().strftime('%-m-%d-%y') + '.csv'
    df_0.to_csv(os.path.join(data_path, file_name))
    
if __name__ == "__main__":
 
    data_files = ["CC_13-03-2020:00:00.csv", "DC_13-03-2020:00:00.csv",
		      "DC_13-03-2020:00:00.csv"]

    # daily file from worldometer
    new_data = '2020-03-15.csv'

    #update and save
    [update_full_data(data_path, full_data, new_data, key) for (key,full_data) in zip(FIELDS.keys(), data_files)]
