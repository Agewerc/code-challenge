import flask

app = flask.Flask(__name__)

@app.route('/', methods= ['GET'])

def home():
    arg = request.args['arg1']
    return 'Hello World'
