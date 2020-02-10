import re

content = 'Extra stings Hello 1234567 World_This is a Rxgex Demo Extra stings'

result1 = re.match('Hello.*?(\d+).*?Demo', content)
print(result1)
result2 = re.search('Hello.*?(\d+).*?Demo', content)
print(result2)

c=input()
