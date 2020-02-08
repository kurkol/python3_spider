import requests

r = requests.get('https://www.taobao.com', timeout = 1)#无限等待设为None
print(r.status_code)

c=input()
