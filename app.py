#!/usr/bin/env python3
from flask import Flask, render_template
from solarCellTestDriver import runEDSTest

app = Flask("SolarBytes")
gpioToCellDictionary = {12 : "1", 16 : "2", 20 : "3", 21 : "4", 6 : "5", 13 : "6", 19 : "7", 26 : "8"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test on cell "+ gpioToCellDictionary[cellSelect]  + " is " + str(ratio)

app.run(debug=True, host='0.0.0.0')
