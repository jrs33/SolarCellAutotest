#!/bin/bash

#
# Runs anything that cannot be done by the GUI for setup 
#
./install.sh
./sql.sh
./buffer.sh

echo "[INFO]	successfully completed install process"
