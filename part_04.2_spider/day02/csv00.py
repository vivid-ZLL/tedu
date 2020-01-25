import csv

with open('fengyun.csv', 'w') as f:
    writer = csv.writer(f)
    # 写一行
    writer.writerow(['alice', 'alicinya'])
    # 写多行
    writer.writerows([('alice02', 'alicinya02'), ('alice03', 'alicinya03')])
