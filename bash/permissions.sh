#!/bin/bash

WPA_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"

# changes files in current directory to executable
function change_bash_permissions() {
	for file in *.sh; do
		echo "$file permissions changed"
		chmod +x $file
	done
}

function change_wpa_permissions() {
	if [ -e $WPA_FILE ]; then
		chmod 777 $WPA_FILE
		"wpa supplicant permissions changed"
	else
		echo "wpa_supplicant file does not exist"
	fi		
}	

# bash function call
change_bash_permissions
change_wpa_permissions
