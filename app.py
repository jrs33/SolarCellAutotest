from flask import Flask, render_template
import os

app = Flask("SolarBytes")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testEDS')
def testEDS():
    average = os.system('./driver.py')
    print('JASDKLASJDLK ' + str(average))
    return 'Test complete'

app.run(debug=True, host='0.0.0.0')
