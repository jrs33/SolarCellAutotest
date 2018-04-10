#!/bin/bash
usb_path=/media/pi/$1
buffer_file=/home/pi/Desktop/.sbByffer.csv
csv_file=solarbytes.csv

function check_usb_connection() {
	if [ -e $usb_path ]; then
		echo "usb connected, porting data now"
		return 0
	else
		echo "usb not connected or uuid is wrong"
		return 1
	fi
}

function check_buffer_exists() {
	if [ -e $buffer_file ]; then
		echo "buffer exists"
		return 0
	else
		echo "buffer does not exist"
		return 1
	fi
}

function remove_old_csv() {
	if [ -e $usb_path/$csv_file ]; then
		rm $usb_path/$csv_file
	fi
}

function port_buffer_file() {
	usb_result=$(check_usb_connection)
	buffer_result=$(check_buffer_exists)
	if [ $usb_result == 1 ]; then
		exit
	fi
	if [ $buffer_result == 1]; then
		exit
	fi
	remove_old_csv
	cp $buffer_file $usb_path
}
