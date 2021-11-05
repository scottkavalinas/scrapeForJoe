import csv
from selenium import webdriver
url ='https://ca.investing.com/commodities/lithium-carbonate-99-min-china-futures-historical-data'
browser = webdriver.Chrome()
browser.get(url)
data = browser.find_element_by_id('curr_table')

f = open("lithium.txt", "a")
f.write(data.text)
f.close()