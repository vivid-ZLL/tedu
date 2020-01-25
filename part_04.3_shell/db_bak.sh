#!/bin/bash

user="root"
passwd="123456"
dbname="mysql"

filename=$(date +%F)-mysql.sql

# 1.创建目录
if [ ! -d "/home/tarena/backup" ];then
	mkdir -p /home/tarena/backup
fi

# 2.开始备份
mysqldump -u$user -p$passwd $dbname > /home/tarena/backup/"$dbname"-${date}.sql

