import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.span())

c=input()
