import csv
with open('data.csv', 'w', newline='') as csvfile:
    #newline=''每行之间没有空格
    writer = csv.writer(csvfile, delimiter=' ')
    #delimiter=' '每列以空格分隔
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '25'])
    #也可用writrows多次写入,二维列表
    #writer.writerows([['10001', 'Mike', '20'], ['10002', 'Bob', '22'], ['10003', 'Jordan', '25']])

with open('data.csv', 'a', newline='') as csvfile:
    #追加写入
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10004','name':'Durant','age':'22'})
    #也可用字典方式写入
