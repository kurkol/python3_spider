import re

content = '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result)
print(result.group(1))

c=input()
#re.I:使匹配对大小写不敏感
#re.L:做本地化识别（locale-aware）匹配
#re.M:多行匹配,影响^和$
#re.S:使.匹配包括换行在内的所有字符
#re.U:根据Unicode字符集解析字符.这个标志影响\w\W\b\B
#re.X:该标志通过基于你更灵活的格式以便你将正则表达式写得更易于理解
