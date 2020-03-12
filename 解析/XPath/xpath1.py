from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link4.html">first item</a></li>
'''

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, "li")]/a/text()')
#contains属性多值匹配

result1 = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
#and多属性匹配

print(result)
print(result1)

c=input()
