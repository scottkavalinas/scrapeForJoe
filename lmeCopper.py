from selenium import webdriver
url ='https://www.argusmedia.com/metals-platform/price/assessment/lme-copper-warehouse-stocks'
browser = webdriver.Chrome()
browser.get(url)
data = browser.find_element_by_id('assessment_price_table_data')
f = open("copper.txt", "a")
f.write(data.text)
f.close()