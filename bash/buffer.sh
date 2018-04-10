#!/bin/bash
buffer_file=/home/pi/Desktop/solarbytes.csv
if [ -e $buffer_file ]; then
	echo $file exists
	exit
fi

touch $buffer_file
echo $buffer_file created
