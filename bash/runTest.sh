#!/bin/bash

FILE="../solarCellTestDriver.py"

# checks for existence of file and runs the test
function run_test_file() {
	if [ -e $FILE ]; then
		./$FILE
		echo "Test complete"
	else
		echo "$FILE does not exist; no test run"
	fi
}

# run command
run_test_file
