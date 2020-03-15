#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:06:15 2020

@author: youssouf
"""

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from os import path, mkdir

data_path = path.dirname(path.abspath(__file__)) + "/data"

if not path.exists(data_path) or not path.isdir(data_path):
    mkdir(data_path)

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")

table_id = 'main_table_countries'
header_tag = 'thead'
head_tag = 'th'
row_tag = 'tr'
col_tag = 'td'

# get the table

table = soup.find(id=table_id)

# get header of the table

headers = table.find_all(header_tag)[0]
headers = headers.find_all(row_tag)[0]
headers = headers.find_all(head_tag)

rows = table.find_all(row_tag) # get all of the rows in the table

now = datetime.now()

with open(data_path + '/' + now.strftime("%d-%m-%Y:%H:%M") + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([header.get_text().replace('</br>', ' ') for header in headers])
    for row in rows:
        cols = row.find_all(col_tag) # get all the columns of the row
        writer.writerow([col.text for col in cols])
