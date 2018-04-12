#!/bin/bash

SUBDOMAIN=solarbytes
NGROK_EXECUTABLE=$1

# checks if ngrok exists and if it does renew the endpoint
function create_tunnel() { 
	go_to_ngrok_file $NGROK_EXECUTABLE
	$NGROK_EXECUTABLE http 5000 #-subdomain=$SUBDOMAIN 5000
}

# sets a flag to 0 if ngrok is not installed
# or 1 if it is installed
function go_to_ngrok_file() {
	cd $1
}

create_tunnel $NGROK_EXECUTABLE
