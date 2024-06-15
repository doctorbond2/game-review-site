from flask import Flask, redirect, request, jsonify
from app import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"
@app.route("/test", methods=['GET'])
def test():
    print("test")
    return redirect("/")
# make visible server = flask --app main run --host=0.0.0.0


if __name__ == "__main__":
    app.run(debug=True)