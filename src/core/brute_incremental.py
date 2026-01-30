import time
import itertools
from core.hash_utils import hash_password,compare_hash

def bruteforce_hash(hash_target, charset, max_length, algo):
    start=time.time()
    attempts = 0
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            attempts +=1
            candidate = "".join(combo)
            candidate_hash = hash_password(candidate,algo)
            if compare_hash(hash_target,candidate_hash):
                elapsed_time=time.time() - start
                return {
                    "found":True,
                    "password" : candidate,
                    "attempts" : attempts,
                    "time" : time
                }
            elapsed = time.time() - start
            return {
                "found": False,
                "password": None,
                "attempts": attempts,
                "time": elapsed
            }