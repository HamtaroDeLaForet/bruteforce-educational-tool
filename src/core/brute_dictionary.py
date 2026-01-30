import time
from core.hash_utils import hash_password, compare_hash

def dictionary_attack(hash_target, dictionary_path, algo):
    start = time.time()
    attempts = 0

    try:
        with open(dictionary_path, "r", encoding="utf-8") as file:
            for line in file:
                candidate = line.strip()

                if not candidate:
                    continue  

                attempts += 1
                candidate_hash = hash_password(candidate, algo)

                if compare_hash(candidate_hash, hash_target):
                    elapsed_time = time.time() - start
                    return {
                        "found": True,
                        "password": candidate,
                        "attempts": attempts,
                        "time": elapsed_time
                    }

    except FileNotFoundError:
        raise FileNotFoundError(f"Dictionary file not found: {dictionary_path}")

    elapsed_time = time.time() - start
    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time": elapsed_time
    }