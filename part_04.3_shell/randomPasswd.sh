#!/bin/bash

key="123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
length=${#key}

for i in {1..8}
do
	index=$[RANDOM%length]
	passwd=$passwd${key:index:1}
done
echo ${passwd}
