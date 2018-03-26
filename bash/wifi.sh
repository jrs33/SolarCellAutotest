#!/bin/bash

WPA_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"
NETWORK_TEXT="./network_template.txt"

# clear the file
function clear_supplicant() {
	local wpa_exists="file_exists $WPA_FILE"
	if [ "$wpa_exists" == 0 ]; then
		" > $WPA_FILE"
	else
		echo "cant clear; supplicant does not exist"
		exit
	fi
}

# pipe text into file
function write_supplicant() {
	local wpa_exists="file_exists $WPA_FILE"
	local network_exists="file_exists $NETWORK_TEXT"
	if [ "$wpa_exists" == 0 ] && [ "$network_exists" == 0 ]; then
		"$NETWORK_TEXT > $WPA_FILE"
		echo "network saved"			
	else
		echo "cant write; supplicant or network file does not exist"
		exit
	fi
}

# check that file exists
function file_exists() {
	if [ -e $1 ]; then
		return 0;
	else
		return 1;
	fi
}

# function calls
clear_supplicant
write_supplicant	
