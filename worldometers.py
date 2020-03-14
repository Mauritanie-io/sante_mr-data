#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:06:15 2020

@author: youssouf
"""

import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path, mkdir

url = "https://www.worldometers.info/coronavirus/"
driver = webdriver.Chrome()
driver.get(url)

data_path = "data"
if not path.exists(data_path) or not path.isdir(data_path):
    mkdir(data_path)

table_id = 'main_table_countries'
header_tag = "thead"
head_tag = "th"
row_tag = "tr"
col_tag = "td"

# get the table

table = driver.find_element(By.ID, table_id)

# get header of the table

headers = table.find_elements(By.TAG_NAME, header_tag)
headers = headers[0].find_elements(By.TAG_NAME, row_tag)
headers = headers[0].find_elements(By.TAG_NAME, head_tag)

rows = table.find_elements(By.TAG_NAME, row_tag) # get all of the rows in the table

now = datetime.now()

with open(data_path + '/' + now.strftime("%d-%m-%Y-%H:%M") + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([header.text.replace('</br>', '') for header in headers])
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, col_tag) # get all the columns of the row
        writer.writerow([col.text for col in cols])


driver.close()
driver.quit()
