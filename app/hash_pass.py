import bcrypt

def encrypt_password(password):
    """ Encrypts the password using bcrypt """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
