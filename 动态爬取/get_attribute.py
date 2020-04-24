from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
zhi_input = browser.find_element_by_id('Popover1-toggle')
print(zhi_input)
print(zhi_input.get_attribute('class'))

#获取文本print(zhi_input.text)
#print(zhi_input.id)
#print(zhi_input.location)
#print(zhi_input.tag_name)
#print(zhi_input.size)
