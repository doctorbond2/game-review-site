from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"


# make visible server = flask --app main run --host=0.0.0.0