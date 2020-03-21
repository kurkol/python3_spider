html = '''
<div id='container'>
<ul class='list'>
<li class="item-0">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

a = doc('.item-0.active a')
print(a.attr('href'))
#获取属性，也可用print(a.attr.href)
#若是选中多个节点可用遍历,for item in a.items():print(item.attr.href)

print(a.text())
print(a.html())
#获取文本；获取HTML文本
