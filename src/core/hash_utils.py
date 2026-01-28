import hashlib

SUPPORTED_HASHES={
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256":hashlib.sha256
}

def hash_password(password:str,algo:str) -> str:
    """
    Compute the hexadecimal hash digest of a plaintext password using a selected hashing algorithm.

    Parameters
    ----------
    password : str
        The plaintext password to hash.
    algo : str
        The name of the hashing algorithm to use. Must be one of the supported algorithms listed in `SUPPORTED_HASHES`.

    Returns
    -------
    str
        The hexadecimal string representation of the password hash.

    Raises
    ------
    ValueError
        If the provided algorithm name is not supported.
    """
    if algo not in SUPPORTED_HASHES:
        raise ValueError(f"Algo {algo} is not supported. "
                         f"Supported algo : {', '.join(SUPPORTED_HASHES.keys())}")
    hash_constructor = SUPPORTED_HASHES[algo]
    hash_obj = hash_constructor()
    password_bytes = password.encode("utf-8")
    hash_obj.update(password_bytes)
    return hash_obj.hexdigest()

def compare_hash(hash1: str, hash2: str) ->bool:
    """
    Compare two hash strings in a case-insensitive manner.

    Parameters
    ----------
    hash1: str
        First hash string.
    hash2 : str
        Second hash string.

    Returns
    -------
    bool
        True if both hashes match (case-insensitive), False otherwise.
    """
    return hash1.lower() == hash2.lower()

def get_supported_hashes() ->list[str]:
    """
    Return supported hash list.

    Returns
    -------
    list[str]
        Supported Hashes list.
    """
    return SUPPORTED_HASHES
