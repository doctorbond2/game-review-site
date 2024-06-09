from flask import Blueprint, request, jsonify
from ..models.user_model import User
from .. import db


def add_user():
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