#!/bin/bash

#
# Script to create buffer csv onboard Pi which will sync to USB and cloud
#
buffer_file=/home/pi/Desktop/solarbytes.csv
if [ -e $buffer_file ]; then
	echo "[WARN]	solarbytes buffer file already exists"
	echo "[INFO]	exiting buffer script"
	exit
fi

touch $buffer_file
echo "[INFO]	buffer file created"
