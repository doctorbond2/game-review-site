from flask import request, jsonify
from ..models.user import User
from .. import db
from security import create_both_tokens
from sqlalchemy import or_
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
    
    if not data.get('username') or not data.get('email'):
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
    session = db.session()

    try:
        if not data.get('username') and  not data.get('email'):
            return jsonify({'message': 'User not found'}),404
        
        user = session.query(User).filter(
            or_(
                User.username == data.get('username'),
                User.email == data.get('email')
            )
        ).first()
        
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        if user.check_password(user,data.get('password')):
            return user
        
        else:
            return jsonify({"message": "Invalid password"}),401
        
    except Exception as e:
        session.rollback()
        return jsonify({'message': 'Something went wrang'}),500
    finally:
        session.close()
def update_user():
    return 'poop'