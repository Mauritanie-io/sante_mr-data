import pandas as pd
from os import path, listdir
from countries import get_country, country_key

file_path = 'data/daily/14-03-2020.csv'

df = pd.read_csv(file_path, sep=",")

for i in df.index:
    country = df[country_key][i]
    df.at[i, country_key] = get_country(country)


df.to_csv(file_path)