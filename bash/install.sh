#!/bin/bash
BUILD_SYSTEM="brew"
WEB_DEV="Flask"
GUI="tkinter"
RPI_GPIO="RPi.GPIO"
DB="sqlite3"

$BUILD_SYSTEM install $WEB_DEV -y
$BUILD_SYSTEM install $GUI -y
$BUILD_SYSTEM install $RPi.GPIO -y
$BUILD_SYSTEM install $DB -y
