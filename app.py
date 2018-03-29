#!/usr/bin/env python
from flask import Flask, render_template, url_for, request, Response
from flask.json import jsonify
from solarCellTestDriver import runEDSTest
from TestingConstants import TestingConstants
from DataTransportFactory import DataTransportFactory
from jinja2 import Environment, PackageLoader
from auth import *

app = Flask("SolarBytes")
constants = TestingConstants()
dataTrans = DataTransportFactory(1)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/testEDS', methods=['GET','POST'])
@requiresAuth
def index():
    return render_template('index.html')

@app.route('/testEDS/<int:cellSelect>')
@requiresAuth
def testEDS(cellSelect):
    ratio = runEDSTest(cellSelect)
    return "Ratio for test on cell "+ constants.PIN_TO_CELL_MAP[cellSelect]  + " is " + str(ratio)

@app.route('/data/table/<limit>')
@requiresAuth
def tableQuery(limit):
    if(limit == ''):
        return dataTrans.transportFromDB(10)
    results = dataTrans.transportFromDB(limit)
    return render_template('data.html', results=results)

@app.route('/data/filter', methods=['POST'])
@requiresAuth
def filterQuery():
    col = request.form.get('column')
    op = request.form.get('operation')
    val = request.form.get('filter')

    if(col == "" or op == "" or val == ""):
        return tableQuery(10)

    results = dataTrans.transportFromDBFiltered(col,op,val,10)
    return render_template('data.html', results=results)

@app.route('/data/aggregate', methods=['POST'])
@requiresAuth
def aggregateQuery():
    col = request.form.get('agg_column')
    op = request.form.get('agg_operation')

    if(col == "" or op == ""):
        return ""

    result = dataTrans.transportFromDBAggregated(col,op)
    return result

@app.route('/data/aggFilter', methods=['POST'])
@requiresAuth
def filterAndAggregateQuery():
    aggCol = request.form.get('agg_column')
    opCol = request.form.get('agg_operation')
    filtCol = request.form.get('filt_column')
    filtOp = request.form.get('filt_operation')
    filtVal = request.form.get('filt_val')

    result = dataTrans.transportFromDBFilterThenAggregate(filtCol,filtOp,filtVal,10,aggCol,opCol)
    return result

app.run(debug=True, host='0.0.0.0')
