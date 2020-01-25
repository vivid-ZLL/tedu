"""
每秒写入一行时间
"""

import time

f = open('log.txt','a+')

# a打开文件偏移在结尾，移动到开头
f.seek(0,0)
n = 0
# 获取现有多少行
for line in f:
    n += 1

while True:
    n += 1
    time.sleep(1)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush() #　随时查看
