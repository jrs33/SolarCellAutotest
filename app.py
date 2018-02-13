#!/usr/bin/env python3
from flask import Flask, render_template
from solarCellTestDriver import runEDSTest
from TestingConstants import TestingConstants

app = Flask("SolarBytes")
constants = TestingConstants()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test on cell "+ constants.PIN_TO_CELL_MAP[cellSelect]  + " is " + str(ratio)

app.run(debug=True, host='0.0.0.0')
