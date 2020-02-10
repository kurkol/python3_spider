import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' }
r = requests.get('https://www.bilibili.com/', headers = headers)

result = re.findall('<a.*?class="name"><span>(.*?)<em>', r.text, re.S)
print(result)

c=input()
