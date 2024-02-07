from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"])

# Get hashed password
def get_password(plain_password):
    return pwd.hash(plain_password)

# Verifying 'Plain password' and "Hashed Password"
def verify_password(plain_password, hashed_password):
    return pwd.verify(plain_password, hashed_password)
