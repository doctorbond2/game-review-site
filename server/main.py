from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"

@app.route("/test", methods=['GET'])
def test():
    return "<p>Test<p/>"
# make visible server = flask --app main run --host=0.0.0.0
