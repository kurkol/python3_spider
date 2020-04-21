#请求
from urllib.parse import urlencode
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
 
def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
     }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

#图片信息
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if title:
                for image in images:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }

#保存图片
import os
from hashlib import md5

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code ==200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloanded', file_path)
    except requests.ConnectionError:
        print('Failed to save Image')

#遍历offset
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

#进程
from multiprocessing.pool import Pool

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START, GROUP_END)])
    pool.map(main, groups)
    pool.close()
    pool.join()

