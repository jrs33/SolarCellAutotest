#!/bin/bash

#
# Runs a test to get ratios of all 4 cells before and after cleaning by the EDS
#
FILE="../solarCellTestDriver.py"
ALL_CELLS=0
USERNAME=""
PASSWORD=""

# checks for existence of file and runs the test
function run_test_file() {
	curl -s -u $USERNAME:$PASSWORD http://localhost:5000/testEDS/$ALL_CELLS > /dev/null
}

# run command
run_test_file
