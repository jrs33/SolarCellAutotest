#!/bin/bash

#
# Renews ngrok tunnel with domain equal to SUBDOMAIN.ngrok.io to connect to open web
#
SUBDOMAIN=solarbytes
NGROK_EXECUTABLE=ngrok

# checks if ngrok exists and if it does renew the endpoint
function create_tunnel() { 
	#go_to_ngrok_file $NGROK_EXECUTABLE
	$NGROK_EXECUTABLE http -subdomain=$SUBDOMAIN -log=stdout 5000 > /dev/null &
}

# sets a flag to 0 if ngrok is not installed
# or 1 if it is installed
function go_to_ngrok_file() {
	cd $1
}

create_tunnel
