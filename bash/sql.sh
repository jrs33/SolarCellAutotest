#!/bin/bash

SQLITE_FILE="../solarbytes.db"
TABLE_NAME="solarTests"

function check_db_exists() {
	local return_flag=1
	if [ -e $SQLITE_FILE ]; then
		local return_flag=0
	fi
	return return_flag
}

function create_database() {
	if [ check_db_exists == 1 ]; then
		touch $SQLITE_FILE
		echo "database created"
	fi
	echo "error: database already exists"
	exit
}

function create_table() {
	sqlite3 $SQLITE_FILE "BEGIN; CREATE TABLE $TABLE_NAME (testDate DATE, testTime TIME, cell INTEGER, ratio FLOAT, temp FLOAT, humidity FLOAT); COMMIT;"
}

create_database
create_table
