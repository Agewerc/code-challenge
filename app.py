import flask
import pandas as pd
from datetime import datetime

data = pd.read_csv('race_dataset.csv', names = ['raceType', 'raceNumber', 'raceName', 'venue', 'raceStartTime']).set_index('raceStartTime')

series = pd.series(index = range(data.raceStartTime.min(), data.raceStartTime.max()))
for m in data.index:
    series.loc[data.loc[m].s:data.loc[m].e] = m

app = flask.Flask(__name__)

@app.route('/', methods= ['GET'])

def home():
    dayTime = request.args['dayTime']
    try:
        return series.loc[dayTime]
    except KeyError
        return f'Invalid Input'



@app.route('')