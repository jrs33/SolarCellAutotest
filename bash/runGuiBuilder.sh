#!/bin/bash

FILE="../setupGUI.py"

# checks for existence of file and runs the test
function run_gui_setup() {
	if [ -e $FILE ]; then
		./$FILE
		echo "GUI setup done"
	else
		echo "$FILE does not exist; no GUI setup"
	fi
}

# run command
run_gui_setup