import argparse
from configs.settings import CHARSETS,DEFAULT_ALGO,DEFAULT_MAX_LENGTH
from core.brute_dictionary import dictionary_attack
from core.brute_incremental import bruteforce_hash
from analysis.time_estimator import estimate_bruteforce_time

def main():
    parser=argparse.ArgumentParser(description="Bruteforce Audit Tool")
    parser.add_argument("--mode",type=str,required=True,choices=["incremental","dictionnary", "estimate"])
    parser.add_argument("--hash",type=str)
    parser.add_argument("--algo",type=str,default=DEFAULT_ALGO)
    parser.add_argument("--charset",type=str,default="digits",choices=CHARSETS.keys())
    parser.add_argument("--max_length",type=int,default=DEFAULT_MAX_LENGTH)
    parser.add_argument("--dict",type=str,)
    parser.add_argument("--password",type=str)
    parser.add_argument("--speed",type=int,default=1_000_000)
    args = parser.parse_args()
    if args.mode == "incremental":
        if not args.hash:
            print("Argument Hash is missing")
            return
        charsets=args.charset
        result=bruteforce_hash(args.hash,charsets,args.max_length,args.algo)
        print(result)
        return
    elif args.mode == "dictionnary":
        if not args.hash:
            print("Argument Hash is missing")
            return
        elif not args.dict:
            print("Argument Dict is missing")
            return
        elif not args.hash and not args.dict:
            print("Arguments Hash & Dict are missig")
            return
        result=dictionary_attack(args.hash,args.dict,args.algo)
        print(result)
        return
    elif args.mode == "estimate":
        if not args.password:
            print("No password was given")
            return
        length=len(args.password)
        charset_size=len(args.charset)
        estimated_time = estimate_bruteforce_time(length,charset_size,args.speed)
        print(estimated_time)
        return
    else:
        print("Error invalid input: mode is not supported")


if __name__ == "__main__":
    main()