import json

data = [{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-10-18"
}]

with open('data1.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    #indent=2表示缩进字符个数,输出为中文需要ensure_ascii=False
