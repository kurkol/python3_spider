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
lis = doc('li').items()
print(lis)
#单个节点可以直接输出，多个节点需要遍历获取
print(type(lis))
for li in lis:
    print(li, type(li))
