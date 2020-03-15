html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')


print(soup.find(class_='element'))
#find_all(name, attrs, recursive, text, **kwargs)
#find_all返回全部元素，find返回第一个匹配元素


print(type(soup.find_all(name="ul")[0]))
for ul in soup.find_all(name="ul"):
    print(ul.find_all(name="li"))
    for li in ul.find_all(name="li"):
        print(li.string)
#find_all(name)

print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
#find_all(attrs)
#也可用print(soup.find_all(id='list-1')),print(soup.find_all(class_='element'))

import re
print(soup.find_all(text=re.compile('Foo')))
#find_all(text)


#find_parent()直接父节点，find_parents()祖先节点
#find_next_siblings(),find_next_sibling()之后兄弟节点
#find_previous_siblings(),find_previous_sibling()之前兄弟节点
#find_all_next(),find_next()选择节点之后节点
#find_all_previous(),find_previous()选择节点之前节点
