#!/bin/bash
DATABASE=../solarbytes.db
SQL_FILE=../sql/solarTests.sql

if [ ! -e $DATABASE ]; then
	touch $DATABASE
	echo "[INFO]	Created solarbytes database"
fi

sqlite3 $DATABASE < $SQL_FILE
echo "[INFO]	Created solarTests table"
