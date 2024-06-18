from flask import Flask, redirect, request, jsonify
from app import app
from app.factory import create_sample_data
@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"
@app.route("/test", methods=['GET'])
def test():
    print("test")
    return redirect("/")
# make visible server = flask --app main run --host=0.0.0.0

print("Running app")
 
with app.app_context():
    create_sample_data()
if __name__ == "__main__":
    app.run(debug=True)