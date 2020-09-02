#!/usr/bin/python
# coding: UTF-8
import datetime
import os

file = open('./resources/template.md')
dir = "./daily/"

if not os.path.exists(dir):
    os.mkdir(dir)
data = file.read()
#print (data)

# 一行ずつ
lines = data.split('\n')
for line in lines:
    print (line)

# 日付取得
name = str(datetime.date.today().strftime("%Y%m%d")) + '.md'

result = open(dir + name, 'w')
result.write(data)