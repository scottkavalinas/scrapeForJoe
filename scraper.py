from selenium import webdriver
url ='https://www.lme.com/Metals/Non-ferrous/LME-Copper#Trading+day+summary'
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('/html/body/main/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div[1]/table').click()