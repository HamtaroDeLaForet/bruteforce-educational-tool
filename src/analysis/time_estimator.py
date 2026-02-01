def estimate_bruteforce_time(length,charset_size, attempts_per_second):
    combinations = charset_size ** length
    seconds= combinations / attempts_per_second
    return {
        "combinations": combinations,
        "seconds": seconds,
        "minutes": seconds / 60,
        "hours": seconds / 3600,
        "days": seconds / 86400,
        "years": seconds / (86400 * 365)
    }