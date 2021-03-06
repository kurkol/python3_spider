html = '''
<div class="wrap">
<div id='container'>
<ul class='list'>
<li class="item-0">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
#选取class为list的节点
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
#CSS选择器中find查找的是子孙节点，只想查找子节点用children()方法

container = items.parent()
print(type(container))
print(container)
print(items.parents('.wrap'))
#parent()父节点，parents()祖先节点

li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))
#siblings()兄弟节点，可以加上筛选条件
