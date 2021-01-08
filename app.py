import flask
import pandas as pd

data = pd.read_csv('race_dataset.csv', names = ['raceType', 'raceNumber', 'raceName', 'venue', 'raceStartTime'])

app = flask.Flask(__name__)
@app.route('/', methods= ['GET'])

def home():
    dayTime = request.args['dayTime']
    try:
         new_data = data[data['raceStartTime'] > dayTime]
         return head(new_data)
    except KeyError
        return f'Invalid Input'