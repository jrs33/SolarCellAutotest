#!/bin/bash

FILE="../solarCellTestDriver.py"
FOURTH_CELL=21
USERNAME=""
PASSWORD=""

# checks for existence of file and runs the test
function run_test_file() {
	curl -s -u $USERNAME:$PASSWORD http://localhost:5000/testEDS/$FOURTH_CELL > /dev/null
}

# run command
run_test_file
