#!/bin/bash
usb_path=/media/pi/$1
buffer_file=/home/pi/Desktop/solarbytes.csv
csv_file=solarbytes.csv

function check_usb_connection() {
	if [ -e $usb_path ]; then
		echo 0
	else
		echo 1
	fi
}

function check_buffer_exists() {
	if [ -e $buffer_file ]; then
		echo 0
	else
		echo 1
	fi
}

function remove_old_csv() {
	csv=$usb_path/$csv_file
	if [ -e $csv ]; then
		rm $csv
	fi
}

function port_buffer_file() {
	usb_result=$(check_usb_connection)
	echo $usb_result
	buffer_result=$(check_buffer_exists)
	echo $buffer_result
	if [ $usb_result == 1 ]; then
		exit
	fi
	if [ $buffer_result == 1 ]; then
		exit
	fi
	remove_old_csv
	cp $buffer_file $usb_path
}

port_buffer_file
