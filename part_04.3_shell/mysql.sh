#!/bin/bash

user="root" 
passwd="123456" 

while : 

do         
	sleep 2         
	count=`mysqladmin  -u"$user"  -p"$passwd" status |  awk '{print $4}'`
	echo "`date +%F` 并发连接数为:$count"

done
