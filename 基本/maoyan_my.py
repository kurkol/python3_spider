import re
import requests

url = 'https://maoyan.com/board/4?offset='
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
movies = []

for i in range(0,10):
	r = requests.get(url+str(i*10), headers=headers)
	result = re.findall('<p class="name"><a.*?>(.*?)</a>', r.text, re.S)
	movies = movies + result

with open('movies.txt','a+') as f:
	f.write(str(movies))
	f.close
