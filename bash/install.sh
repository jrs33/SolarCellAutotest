#!/bin/bash
BUILD_SYSTEM="apt-get"
WEB_DEV="Flask"
GUI="tkinter"
RPI_GPIO="RPi.GPIO"
DB="sqlite3"
XTERM="xterm"

# check if a package is installed and if it isnt
# install the package
function install_package() {
	local return_val=1
	type $1 >/dev/null 2>&1 || { local return_val=0; }
	if [ return_val == 1 ]; then
		$BUILD_SYSTEM update
		$BUILD_SYSTEM install $1 -y
		echo "installed $1"
	else
		echo "$1 already installed or could not install"
	fi
}

# calls to install various packages
install_package $WEB_DEV
install_package $GUI
install_package $RPI_GPIO
install_package $DB
install_package $XTERM
