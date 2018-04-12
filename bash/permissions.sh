#!/bin/bash

WPA_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"

# changes files in current directory to executable
function change_bash_permissions() {
	for file in *.sh; do
		echo "[INFO]	$file permissions changed"
		chmod +x $file
	done
}

function change_wpa_permissions() {
	if [ -e $WPA_FILE ]; then
		sudo chmod 777 $WPA_FILE
		echo "[INFO]	wpa_supplicant permissions changed"
	else
		echo "[INFO]	wpa_supplicant file does not exist"
	fi		
}	

# bash function call
change_bash_permissions
change_wpa_permissions
chmod 777 network_template.txt
