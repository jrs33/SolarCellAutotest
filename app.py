from flask import Flask, render_template
import os

app = Flask("SolarBytes")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS')
def testEDS():
    os.system('./driver.py')
    return 'Test complete'

app.run(debug=True, host='0.0.0.0')
