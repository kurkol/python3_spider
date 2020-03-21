import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

html = requests.get(url, headers = headers).text
doc = pq(html)

items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.text', 'a', encoding='urf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n'+'=' * 50 +'\n')
    file.close()

#打开方式：
#r：只读，指针在开头
#rb：二进制只读，指针在开头
#r+：读写，指针在开头
#rb+：二进制读写，指针在开头
#w：写入，覆盖原文件，文件不存在时创建新文件
#wb：二进制写入，覆盖原文件，文件不存在时创建新文件
#w+：读写，覆盖原文件，文件不存在时创建新文件
#wb+：二进制读写，覆盖原文件，文件不存在时创建新文件
#a：追加方式打开，指针在结尾，文件不存在时创建新文件
#ab：二进制追加，指针在结尾，文件不存在时创建新文件
#a+:读写方式打开，指针在结尾，文件不存在时创建新文件
#ab+：二进制追加方式打开，指针在结尾，文件不存在时创建新文件
