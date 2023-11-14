from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import json

csv_path = 'OutBound_Data/Outbound_10Y_data.csv'

# 올바른 함수 이름은 read_csv 입니다. read_scv는 오타입니다.
df = pd.read_csv(csv_path)

country_list = df.columns.tolist()

print(country_list)