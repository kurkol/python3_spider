html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
</p>
<p class="story">...</p>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

print(soup.a.parent)
#parent取直接父节点

print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
#parents取祖先节点

print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
#获取节点的下一个和上一个元素
print('Next Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Sibling', list(enumerate(soup.a.previous_siblings)))
#获取后面和前面的兄弟节点
