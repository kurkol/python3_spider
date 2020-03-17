html = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))


doc = pq(url='https://cuiqingcai.com')
print(doc('title'))
#从url获取

doc = pq(filename='demo.html')
print(doc('li'))
#从文件获取
