import hashlib
import os
import tempfile
import pytest
from src.core.brute_dictionary import dictionary_attack

def create_temp_dict(words):
    fd, path = tempfile.mkstemp(text=True)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        for w in words:
            f.write(w + "\n")
    return path

def test_dictionary_attack_finds_password():
    password = "secret"
    hash_target = hashlib.sha256(password.encode("utf-8")).hexdigest()
    dict_path = create_temp_dict(["hello", "secret", "world"])

    result = dictionary_attack(hash_target, dict_path, algo="sha256")
    assert result["found"] is True
    assert result["password"] == password
    assert result["attempts"] > 0
    assert result["time"] > 0

    os.remove(dict_path)

def test_dictionary_attack_not_found():
    password = "secret"
    hash_target = hashlib.sha256(password.encode("utf-8")).hexdigest()
    dict_path = create_temp_dict(["hello", "world"])

    result = dictionary_attack(hash_target, dict_path, algo="sha256")
    assert result["found"] is False
    assert result["password"] is None

    os.remove(dict_path)

def test_dictionary_attack_empty_file():
    dict_path = create_temp_dict([])
    hash_target = hashlib.sha256("anything".encode("utf-8")).hexdigest()

    result = dictionary_attack(hash_target, dict_path, algo="sha256")
    assert result["found"] is False
    assert result["password"] is None
    assert result["attempts"] == 0

    os.remove(dict_path)

def test_dictionary_attack_file_not_found():
    with pytest.raises(FileNotFoundError):
        dictionary_attack("abcd", "nonexistent.txt", algo="sha256")
