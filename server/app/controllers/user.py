from flask import request, jsonify
from ..models.user import User
from .. import db


def user_data_receiver():
    data = request.get_json()
    user = {
        'username': data.get('username'),
        'email': data.get('email'),
        'password' : data.get('password'),
        'rating' : data.get('rating')
    }
    return user
def add_user():
    data = user_data_receiver()
    
    if not data['username'] or not data['email']:
        return jsonify({'error': 'Please provide username and email'}), 400
    
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        print("add triggered")
    except Exception as e:
        db.session.rollback()  
        return jsonify({"error": str(e)}), 500
    return '<p>add user<p/>'

def login_user():
    data = user_data_receiver()
def update_user():
    return 'poop'