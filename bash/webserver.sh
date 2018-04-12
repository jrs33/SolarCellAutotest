#!/bin/bash

APP_DIRECTORY="../app/"
APP_FILE="app.py"
APP_FILE_REL_LOC=$APP_DIRECTORY$APP_FILE

# start the web server by running the python script
function start_server() {
	if [ -e $APP_FILE_REL_LOC ]; then
		cd $APP_DIRECTORY
		echo "[INFO]	starting up server..."
		./$APP_FILE
	else
		echo "[ERROR]	app file not found"
	fi
}

# call bash function
start_server
