from flask import Flask, render_template, request, url_for, redirect, flash
from influxdb import InfluxDBClient
from dotenv import load_dotenv
import os, re

load_dotenv()

INFLUXIP = os.getenv('INFLUXHOST')
INFLUXPORT = os.getenv('INFLUXPORT')
USER = os.getenv('USERNAME')
PASS = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

data = [
                {
                 "measurement": "your_measurement",
                 "tags": {
                     "key": "value"
                     },
                 "fields": {
                     "value": "sample_value"
                     }
                }
                ]


app = Flask(__name__)
client = InfluxDBClient(host=INFLUXIP, port=INFLUXPORT, database=DATABASE, username=USER, password=PASS)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form['value']
        if re.search("^\d+[\.\,]?\d*$", value) != None:
            
            # Code for InfluxDB here
            data = [
                {
                 "measurement": "your_measurement",
                 "tags": {
                     "key": "value"
                     },
                 "fields": {
                     "value": value
                     }
                }
                ]

            client.write_points(data)

            feedback = "wrote data to database"
            return render_template('submit.html', feedback=feedback, color="green")
        else:
            feedback = 'value is not numeric or decimal'
            return render_template('submit.html', feedback=feedback, color="red")
    else:
        return render_template('submit.html')

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'some secret key'
