#!/bin/bash
buffer_file=/home/pi/Desktop/.sbBuffer.csv
if [ -e $buffer_file ]; then
	echo $file exists
	exit
fi

touch $buffer_file
echo $buffer_file created
