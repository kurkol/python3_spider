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
