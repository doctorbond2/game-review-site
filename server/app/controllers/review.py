from flask import request
from app import db

def add_one_new_review_from_user():
    session = db.session()
    
        