from src.configs.settings import CHARSETS, DEFAULT_ALGO, DEFAULT_MAX_LENGTH
from src.core.hash_utils import SUPPORTED_HASHES

def test_charsets_structure():
    assert isinstance(CHARSETS, dict)
    for key, value in CHARSETS.items():
        assert isinstance(value, str)

def test_default_algo():
    assert isinstance(DEFAULT_ALGO, str)
    assert DEFAULT_ALGO in SUPPORTED_HASHES

def test_default_max_length():
    assert isinstance(DEFAULT_MAX_LENGTH, int)
    assert DEFAULT_MAX_LENGTH > 0
