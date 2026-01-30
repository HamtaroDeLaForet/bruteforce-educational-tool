def estimate_bruteforce_time(length,charset_size, attempts_per_second):
    combinations = charset_size ** length
    seconds= combinations / attempts_per_second
    minutes = seconds / 60
    hours = seconds / 3600
    days = seconds / 86400
    years = seconds / 31540000
    return {
        "combinations ": combinations,
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days,
        "years": years
    }