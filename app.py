#!/usr/bin/env python3
from flask import Flask, render_template
from driver import runEDSTest

app = Flask("SolarBytes")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test is " + str(ratio)

app.run(debug=True, host='0.0.0.0')
