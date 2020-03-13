html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

print(soup.prettify())
#把要解析的字符串以标准缩进格式输出

print(soup.title)
#输出title节点全部内容
print(type(soup.title))
print(soup.p)
#只输出第一个p节点

print(soup.title.string)
#用.string输出节点包含的文本内容

print(soup.title.name)
#输出title节点名称

print(soup.p.attrs)
print(soup.p.attrs['name'])
#获取属性
#也可直接print(soup.p['name'])




