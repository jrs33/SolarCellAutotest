#!/bin/bash

./permissions.sh
./install.sh
./sql.sh
./buffer.sh
./wifi.sh

echo "[INFO]	successfully completed install process"
echo "[INFO]	rebooting now so changes take system-wide effect"
echo "[INFO]	shutting down..."
sleep 5
sudo reboot
