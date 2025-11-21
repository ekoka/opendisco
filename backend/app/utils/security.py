from argon2 import PasswordHasher

from app.utils.string import unicode_normalizer

pw_hasher = PasswordHasher()

def hash_password(password: bytes|str):
    if type(password) is str:
        unicode_normalizer(password)
        password = password.encode('utf-8')
    # no need to explicitly salt, done automatically.
    pwhash = pw_hasher.hash(password)
    return pwhash.decode('utf-8')

