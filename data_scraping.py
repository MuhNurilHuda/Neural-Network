import requests
import time
import csv
# import streamlit as st
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://harga-emas.org/history-harga/2023/Mei/20/'
driver = webdriver.ChromeOptions()
driver.add_argument("--start-maximized")
driver = webdriver.Chrome(options=driver)
driver.get(url)
response = requests.get(url)
html_content = response.text
time.sleep(2)
soup = BeautifulSoup(html_content, "html.parser")
scraped_data = []

# Selecting the date
date_element = soup.findAll('table', 'in_table')
date_element2 = date_element[0].findAll('tr')
# date_element3 = date_element2.findAll('tr')
# print(len(date_element2))

for i in range(0, 5):
    for data in date_element2:
        date_row = data.findAll('td')
        print("Jumlah td per baris : ")
        print(len(date_row))
    
        for date in date_row:
            pick_date = date.findAll('a')
            print(len(pick_date))
    
    driver.find_element(By.CSS_SELECTOR, "a").click()
    print("Ganti Halaman")
    
# # Selecting price data from table
# div_element = soup.findAll('div', 'row space30')
# div_element2 = div_element[2].findAll('div', 'col-md-8')
# div_element3 = div_element2[0].findAll('table', 'in_table')
# div_element4 = div_element3[1].findAll('tr')

# print(len(div_element4))

# data=[]
# for data in div_element4:
#     div_element5 = data.findAll('td')
#     print(len(div_element5))

# for data in div_element4:
#     div_element5 = data.findAll('td')
#     div_element6 = div_element5[1]
#     text_element2 = div_element6.get_text(strip=True)
#     st.text(text_element2)
#     scraped_data.append(text_element2)
    
# # Define the CSV file path
# csv_file = 'scraped_data.csv'

# # Open the CSV file in write mode
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write the header row (If applicable)
#     writer.writerow(['20 Mei 2023'])
    
#     # Write the data rows
#     for data in scraped_data:
#         writer.writerow([data])