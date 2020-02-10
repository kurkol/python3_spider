import re

content = 'Hello 1234567 Word_This is a Regex Demo'

result1 = re.match('^He.*(\d+).*Demo$', content)
print(result1.group(1))
result2 = re.match('^He.*?(\d+).*Demo$', content)
print(result2.group(1))

c=input()
