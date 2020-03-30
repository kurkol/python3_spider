import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



#也可用pandas的read_cvs读取
#import pandas as pd
#df = pd.read_csv('data.csv')
#print(df)
