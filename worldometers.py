#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:06:15 2020

@author: youssouf
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from os import path, mkdir
import pandas as pd

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")    
    return soup

def get_table(soup, table_id):
    return soup.find(id=table_id)

def parse_table_tocsv(table, csvfile):
    # get header of the table
    headers = table.find_all(header_tag)[0]
    headers = headers.find_all(row_tag)[0]
    headers = headers.find_all(head_tag)
    
    df_headers = [header.get_text().replace('</br>', ' ') for header in headers]
    
    rows = table.find_all(row_tag) # get all of the rows in the table
    df_rows = []
    for row in rows:
        cols = row.find_all(col_tag) # get all the columns of the row
        df_cols = [col.get_text() for col in cols]
        df_rows.append(df_cols)
        
    df = pd.DataFrame(data=df_rows, columns = df_headers)
    df.to_csv(csvfile, index=False, header=True)

data_path = path.dirname(path.abspath(__file__)) + "/data"

url = "https://www.worldometers.info/coronavirus/"

table_id = 'main_table_countries'
header_tag = 'thead'
head_tag = 'th'
row_tag = 'tr'
col_tag = 'td'

if __name__ == "__main__":
    
    # Check if the data path exists
    if not path.exists(data_path) or not path.isdir(data_path):
        mkdir(data_path)
        
    # get page source
    soup = get_page(url)

    # get the table
    table = get_table(soup, table_id)
    
    # get the time now
    now = datetime.now()
    
    # name the csvfile using the time now
    csvfile = data_path + '/' + now.strftime("%d-%m-%Y") + '.csv'
    
    # parse the table into a csvfile
    parse_table_tocsv(table, csvfile)