import pytest
import hashlib
from src.core.brute_incremental import bruteforce_hash

def test_hash_password_found():
    password = "abc123"
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    charset = "abcdefghijklmnop123456789"
    max_length = 8
    algo = "sha256"
    result = bruteforce_hash(password_hash,charset,max_length,algo)
    assert result["found"] == True
    assert result["password"] == password
    assert result["attempts"] > 0
    assert result["time"] > 0
    
def test_hash_password_not_found():
    password = "abc123"
    password_hash = "nope"
    charset = "abcdefghijklmnopqrstuvwxyz"
    max_length = 5
    algo = "sha256"
    result = bruteforce_hash(password_hash,charset,max_length,algo)
    assert result["found"] == False
    assert result["password"] == None
    
def test_hash_password_maxlength_not_in_range():
    password = "abc123"
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    charset = "abcdefghijklmnop123456789"
    max_length = 2
    algo = "sha256"
    result = bruteforce_hash(password_hash,charset,max_length,algo)
    assert result["found"] == False
    
def test_hash_password_empty_charset():
    password = "abc123"
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    charset = ""
    max_length = 2
    algo = "sha256"
    result = bruteforce_hash(password_hash,charset,max_length,algo)
    assert result["found"] is False
    assert result["password"] is None
    assert result["attempts"] == 0