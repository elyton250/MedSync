import bcrypt

def encrypt_password(password):
    """ Encrypts the password using bcrypt """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(hashed_password, password):
    """ Check the hashed password against the provided password """
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
