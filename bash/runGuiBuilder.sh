#!/bin/bash

FILE="../gui/setupGUI.py"

# checks for existence of file and runs the test
function run_gui_setup() {
	if [ -e $FILE ]; then
		echo "[INFO]	opening gui..."
		./$FILE
		echo "[INFO]	gui terminated"
	else
		echo "[ERROR]	gui runner does not exist; no GUI setup"
	fi
}

# run command
run_gui_setup
