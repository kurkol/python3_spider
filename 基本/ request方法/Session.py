import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456798')
r = s.get('http://httpbin.org/cookies')
print(r.text)

c=input()
