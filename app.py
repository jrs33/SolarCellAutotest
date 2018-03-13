#!/usr/bin/env python3
import sqlite3
from flask import Flask, render_template
from solarCellTestDriver import runEDSTest
from flask_sqlalchemy import SQLAlchemy
from TestingConstants import TestingConstants

app = Flask("SolarBytes")
constants = TestingConstants()
db = sqlite3.connect(constants.SQL_DATABASE)
sqlFactory = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test on cell "+ constants.PIN_TO_CELL_MAP[cellSelect]  + " is " + str(ratio)

app.run(debug=True, host='0.0.0.0')
