import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token
def hash_password(pw):
    pw_bytes = pw.encode('utf-8')

    salt = bcrypt.gensalt(12)

    hashed_pw = bcrypt.hashpw(pw, salt)

    return hashed_pw


def verify_password(pw, hashed_pw):

    pw_bytes = pw.encode('utf-8')

    return bcrypt.checkpw(pw_bytes,pw)

def create_both_tokens(user):
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    return {
        'access_token' :access_token,
        'refresh_token': refresh_token
    }

