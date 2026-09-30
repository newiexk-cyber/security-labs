import pytest
from securecrypto import hash_utils
from argon2.exceptions import VerifyMismatchError

def test_hash_password_and_verify():
    raw_pwd = "StrongPass123!"
    hashed = hash_utils.hash_password_secure(raw_pwd)
    assert hashed is not None

    from argon2 import PasswordHasher
    ph = PasswordHasher()
    try:
        ph.verify(hashed, raw_pwd)
        verified = True
    except VerifyMismatchError:
        verified = False
    assert verified == True

def test_wrong_password_verification():
    raw_pwd = "CorrectPass"
    wrong_pwd = "WrongPass"
    hashed = hash_utils.hash_password_secure(raw_pwd)

    from argon2 import PasswordHasher
    ph = PasswordHasher()
    try:
        ph.verify(hashed, wrong_pwd)
        verified = True
    except VerifyMismatchError:
        verified = False
    assert verified == False


