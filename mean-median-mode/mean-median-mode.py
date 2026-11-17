from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = sorted(x)
    n = len(x)
    half = int(n/2)
    mean = sum(x) / n

    if n%2==0:
        median = float((x[half-1] + x[half]) / 2)
    else:
        median = float(x[half])

    counts = Counter(x)
    freq = max(counts.values())
    mode = min(float(num) for num, value in counts.items() if value==freq)

    return {"mean":mean, "median":median, "mode":mode}
    