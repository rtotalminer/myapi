import bcrypt

def hash_pass(pwd):
    pwd = pwd.encode('utf-8')
    return bcrypt.hashpw(pwd, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    pwd = plain_text_password.encode('utf-8')
    print(plain_text_password, pwd, hashed_password)
    return bcrypt.checkpw(pwd, hashed_password)