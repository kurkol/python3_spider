#Ajax获取李文亮前十页微博
#请求
from urllib.parse import urlencode
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Hoset':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/1139098205',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-with':'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type':'uid',
        'value':'1139098205',
        'containerid':'1076031139098205',
        'page':page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

#解析
from pyquery import PyQuery as pq

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

#遍历微博
if __name__ == '__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
