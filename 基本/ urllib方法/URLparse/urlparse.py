from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', scheme='http', allow_fragments=True)
print(type(result), result)

c=input()
