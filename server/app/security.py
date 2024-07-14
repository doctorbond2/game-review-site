import bcrypt

def hash_password(pw):
    pw_bytes = pw.encode('utf-8')

    salt = bcrypt.gensalt(12)

    hashed_pw = bcrypt.hashpw(pw, salt)

    return hashed_pw


def verify_password(pw, hashed_pw):

    pw_bytes = pw.encode('utf-8')

    return bcrypt.checkpw(pw_bytes,pw)

