#!/bin/bash
for i in $(ls ~/1905/shell/token.conf)
do
	md5sum "$i" >> ~/1905/shell/md5log.txt
done

