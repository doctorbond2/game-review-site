from flask import Flask, redirect
from app import create_app
from flask_sqlalchemy import SQLAlchemy
app = create_app()
db = SQLAlchemy(app) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

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