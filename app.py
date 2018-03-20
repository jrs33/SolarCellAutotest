#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request
from flask.json import jsonify
from solarCellTestDriver import runEDSTest
from TestingConstants import TestingConstants
from DataTransportFactory import DataTransportFactory
from jinja2 import Environment, PackageLoader, select_autoescape

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

@app.route('/data/table/<limit>')
def tableQuery(limit):
    if(limit == ''):
        return dataTrans.transportFromDB(10)
    results = dataTrans.transportFromDB(limit)
    return render_template('data.html', results=results)

@app.route('/data/filter', methods=['POST'])
def filterQuery():
    col = request.form.get('column')
    op = request.form.get('operation')
    val = request.form.get('filter')

    if(col == "" or op == "" or val == ""):
        return tableQuery(10)
    
    results = dataTrans.transportFromDBFiltered(col,op,val,10)
    return render_template('data.html', results=results)

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
