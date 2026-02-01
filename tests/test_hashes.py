import pytest
import hashlib
from src.core.hash_utils import(hash_password,compare_hash,get_supported_hashes,SUPPORTED_HASHES)

def test_hash_password_valid_algo():
    password="test123"
    algo="sha256"
    result = hash_password(password,algo)
    expected = hashlib.sha256(password.encode("utf-8")).hexdigest()
    assert result == expected

def test_hash_password_invalid_algo():
    with pytest.raises(ValueError):
        hash_password("test","bcrypt")

def test_hash_password_case_insensitive():
    h1 = "ABCDEF"
    h2 = "abcdef"
    assert compare_hash(h1,h2) is True

def test_compare_hash_not_equal():
    assert compare_hash("abc","def") is False
    
def test_get_supported_hashes():
    assert get_supported_hashes() == SUPPORTED_HASHES
    assert "sha256" in get_supported_hashes()