import flask
from flask import request
import pandas as pd

data = pd.read_csv('race_dataset.csv', names=['raceType', 'raceNumber', 'raceName', 'venue', 'raceStartTime'])

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    dayTime = float(request.args['dayTime'])
    try:
        return dayTime#data[data['raceStartTime'] > dayTime].head()
    except KeyError:
        return 'Invalid Input'
