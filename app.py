from flask import Flask
import os

app = Flask("SolarBytes")

@app.route('/')
def index():
    return 'SolarBytes'

@app.route('/testEDS')
def testEDS():
    os.system('./driver.py')
    return 'Test complete'

app.run(debug=True, host='0.0.0.0')
