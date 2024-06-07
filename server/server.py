from flask import Flask, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
print("Running main.py")
@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"

@app.route("/test", methods=['GET'])
def test():
    print("test")
    return "<p>Test<p/> "
# make visible server = flask --app main run --host=0.0.0.0

if __name__ == "__main__":
    app.run(debug=True)