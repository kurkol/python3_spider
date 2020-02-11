import re

content = '5fds4af4dsf4d'
result = re.sub('\d', '', content)

with open('sub.txt','a+') as f:
	f.write(result)
	f.close
	
