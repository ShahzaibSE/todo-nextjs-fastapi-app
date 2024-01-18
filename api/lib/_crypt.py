from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated=True)

# Get hashed password
def get_password(plain_password: str):
    return pwd.hash(plain_password)

# Verifying 'Plain password' and "Hashed Password"
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)
