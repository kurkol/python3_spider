from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.taobao.com')

#单节点
input_first = browser.find_element_by_name('q')
input_second = browser.find_elements_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
#find_element_by_id("name")等价于find_element(By.id,'name')
input_foured = browser.find_element(By.NAME, 'q')

print(input_first, '\n', input_second, '\n', input_third, '\n', input_foured, '\n')
#多个节点

input_mult = browser.find_elements_by_css_selector('.service-bd li')

print(input_mult)

browser.close()
