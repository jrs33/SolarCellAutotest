#!/usr/bin/env python3
from flask import Flask, render_template
from solarCellTestDriver import runEDSTest
from TestingConstants import TestingConstants
from DataTransportFactory import DataTransportFactory

app = Flask("SolarBytes")
constants = TestingConstants()
dataTrans = DataTransportFactory(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test on cell "+ constants.PIN_TO_CELL_MAP[cellSelect]  + " is " + str(ratio)

@app.route('/data/filter/<str:col>/<str:op>/<str:val>')
def filterQuery(op,
                col,
                val):
    if(op == null or col == null or val == null):
        return null
    
    if(request.args.get('limit')): # query parameter
        lim = request.args.get('limit')
        return dataTrans.transportFromDBFiltered(col,op,val,lim)
    return dataTrans.transportFromDBFiltered(col,op,val,10)

@app.route('/data/aggregate/<str:col>/<str:op>')
def filterQuery(op,
                col):
    if(op == null or col == null):
        return null
    
    if(request.args.get('limit')): # query parameter
        lim = request.args.get('limit')
        return dataTrans.transportFromDBAggregated(col,op,lim)
    return dataTrans.transportFromDBAggregated(col,op,10)

app.run(debug=True, host='0.0.0.0')
