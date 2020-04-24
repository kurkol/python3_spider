from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')

#输入框
input = browser.find_element_by_id('kw')
#按键
button = browser.find_element_by_id('su')
#输入文字
input.send_keys('Python')
#点击按钮
button.click()
#清空输入框
input.clear()

browser.close()
