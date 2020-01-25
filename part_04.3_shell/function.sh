#!/bin/bash

f1(){
	echo "Lord Alice!!"
}

f1

sumn(){
	echo $[n1+n2]
}

subn(){
	echo $[n1-n2]	
}

read -p "number 1:" n1
read -p "number 2:" n2
read -p "option(+|-):" op

case $op in
"+"):
	sumn
	;;

"-"):
	subn
	;;
*):
	echo "Invalid option"

esac







