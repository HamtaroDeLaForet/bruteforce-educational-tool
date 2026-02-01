import time
import itertools
from .hash_utils import hash_password,compare_hash

def bruteforce_hash(hash_target, charset, max_length, algo):
    start = time.time()
    attempts = 0

    if not charset or max_length < 1:
        return {
            "found": False,
            "password": None,
            "attempts": 0,
            "time": 0
        }

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            attempts += 1
            candidate = "".join(combo)
            candidate_hash = hash_password(candidate, algo)

            if compare_hash(hash_target, candidate_hash):
                elapsed = time.time() - start
                return {
                    "found": True,
                    "password": candidate,
                    "attempts": attempts,
                    "time": elapsed
                }

    elapsed = time.time() - start
    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time": elapsed
    }