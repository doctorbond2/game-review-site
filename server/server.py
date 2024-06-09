from flask import Flask, redirect, request, jsonify
from app import create_app
from flask_sqlalchemy import SQLAlchemy
app = create_app()
db = SQLAlchemy(app) 

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)



@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"
@app.route("/test", methods=['GET'])
def test():
    print("test")
    return redirect("/")
# make visible server = flask --app main run --host=0.0.0.0


@app.route("/add", methods=['POST'])
def add_something():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    print(username)
    
    if not username or not email:
        return jsonify({'error': 'Please provide username and email'}), 400
    new_user = Users(username=username, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
        print("add triggered")
    except Exception as e:
        db.session.rollback()  
        return jsonify({"error": str(e)}), 500
    return '<p>add user<p/>'
if __name__ == "__main__":
    app.run(debug=True)