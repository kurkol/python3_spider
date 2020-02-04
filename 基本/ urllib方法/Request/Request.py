from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
	'Host':'httpbin.org'
}
dict={
	'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

c=input()
