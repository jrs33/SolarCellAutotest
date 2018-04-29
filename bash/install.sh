#!/bin/bash

#
# Installs all required dependencies to connect Pi to Solarbytes hardware
#
BUILD_SYSTEM="pip3"
WEB_DEV="Flask"
GUI="tkinter"
RPI_GPIO="RPi.GPIO"
DB="sqlite3"
XTERM="xterm"
BOTO="boto3"
AWSCLI="awscli"

# check if a package is installed and if it isnt
# install the package
function install_package() {
	local return_val=1
	type $1 >/dev/null 2>&1 || { local return_val=0; }
	if [ return_val == 1 ]; then
		$BUILD_SYSTEM install $1
		echo "[INFO]	installed $1"
	else
		echo "[WARN]	$1 already installed or could not install"
	fi
}

sudo apt-get install python3-pip

# install the following packages into python3
install_package $WEB_DEV
install_package $GUI
install_package $RPI_GPIO
install_package $DB
install_package $XTERM
install_package $BOTO
install_package $AWSCLI

sudo $BUILD_SYSTEM install git build-essential python-pip python-dev python-smbus

git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
sudo python setup.py install
cd ..

git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
cd ..

sudo rm -r Adafruit_Python_MCP3008
sudo rm -r Adafruit_Python_GPIO
