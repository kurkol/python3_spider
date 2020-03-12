from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//*')
#result = html.xpath('//li')
#result = html.xpath('//li/a')
#//获取直接子节点，/获取子孙节点

result1 = html.xpath('//a[@href="link4.html"]/../@class')
#..获取父节点
#result1 = html.xpath('//a[@href="link4.html"]/parent::*/@class')也可

result2 = html.xpath('//li[@class="item-0"]')
#属性过滤

result3 = html.xpath('//li[@class="item-0"]/a/text()')
#text()获取文本

result4 = html.xpath('//li/a/@href')
#@获取属性


print(result)
print(result1)
print(result2)
print(result3)
print(result4)

c=input()
