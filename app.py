from flask import Flask, render_template, request, url_for, redirect, flash
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form['value']
        print(re.search("^\d+[\.\,]?\d*$", value))
        if re.search("^\d+[\.\,]?\d*$", value) != None:
            # Code for InfluxDB here
            

            return render_template('submit.html')
        else:
            feedback = 'value is not numeric or decimal'
            print(feedback)
            return render_template('submit.html', feedback=feedback)
    else:
        return render_template('submit.html')

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'some secret key'
