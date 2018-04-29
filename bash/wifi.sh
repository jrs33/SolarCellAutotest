#!/bin/bash

#
# Sets up auto-connection to wifi using network_template.txt network object credentials
#
WPA_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"
NETWORK_TEXT="./network_template.txt"

# clear the file
function clear_supplicant_write_network() {
	wpa_exists=$(file_exists $WPA_FILE)
	network_exists=$(file_exists $NETWORK_TEXT)
	if [ $wpa_exists -eq 0 ] && [ $network_exists -eq 0 ]; then
		 > $WPA_FILE
		echo "[INFO]	cleared supplicant file succesfully"
		$NETWORK_TEXT > $WPA_FILE
		exit
	else
		echo "[ERROR]	cant clear; supplicant does not exist"
		exit
	fi
}

# check that file exists
function file_exists() {
	if [ -e $1 ]; then
		echo 0;
	else
		echo 1;
	fi
}

# function calls
clear_supplicant_write_network
