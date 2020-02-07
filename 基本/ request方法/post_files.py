import requests

files = {'files':open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

c=input()
