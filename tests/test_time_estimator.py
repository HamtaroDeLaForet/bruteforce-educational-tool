from src.analysis.time_estimator import estimate_bruteforce_time

def test_estimate_combinations():
    result = estimate_bruteforce_time(length=4, charset_size=10, attempts_per_second=1_000_000)
    assert result["combinations"] == 10_000
    assert result["seconds"] > 0
    assert result["minutes"] == result["seconds"] / 60
    assert result["hours"] == result["seconds"] / 3600
    assert result["days"] == result["seconds"] / 86400
    assert result["years"] == result["seconds"] / (86400 * 365)
