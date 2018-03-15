#!/usr/bin/env python3
from flask import Flask, render_template
from flask.json import jsonify
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

@app.route('/testInsert')
def testInsert():
    dataTrans.transportToDB()
    return "INSERTED DATA!"

@app.route('/data/table/<limit>')
def tableQuery(limit):
    if(limit == ''):
        return dataTrans.transportFromDB(10)
    return jsonify({'rows': dataTrans.transportFromDB(limit)})

@app.route('/data/filter/<op>/<col>/<val>')
def filterQuery(op,
                col,
                val):
    if(op == '' or col == '' or val == ''):
        return null
    
    '''if(request.args.get('limit')): # query parameter
        lim = request.args.get('limit')
        return dataTrans.transportFromDBFiltered(col,op,val,lim)'''
    return jsonify({'rows': dataTrans.transportFromDBFiltered(col,op,val,10)})

@app.route('/data/aggregate/<op>/<col>')
def aggregateQuery(op,
                   col):
    if(op == '' or col == ''):
        return null
    
    if(request.args.get('limit')): # query parameter
        lim = request.args.get('limit')
        return dataTrans.transportFromDBAggregated(col,op,lim)
    return jsonify({'rows': dataTrans.transportFromDBAggregated(col,op,10)})

app.run(debug=True, host='0.0.0.0')
