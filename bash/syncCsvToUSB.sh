##!/bin/bash
USB_UUID_FROM_DISPLAY_MOUNTS=""
usb_path=/media/pi/$USB_UUID_FROM_DISPLAY_MOUNTS
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
	buffer_result=$(check_buffer_exists)
	if [ $usb_result == 1 ]; then
		echo "[ERROR]	USB not connected or uuid entered incorrectly. Try ./displayMounts to see the uuid."
		exit
	fi
	if [ $buffer_result == 1 ]; then
		echo "[ERROR]	Buffer csv does not exist"
		exit
	fi
	remove_old_csv
	cp $buffer_file $usb_path
	echo "[INFO]	Successfully synced buffer data with usb"
}

port_buffer_file
