from passlib.context import CryptContext

cpwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return cpwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return cpwd_context.hash(password)
