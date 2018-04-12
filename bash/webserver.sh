#!/bin/bash

APP_FILE="../app.py"

# start the web server by running the python script
function start_server() {
	if [ -e $APP_FILE ]; then
		./$APP_FILE
	else
		echo "app file not found"
	fi
}

# call bash function
start_server
