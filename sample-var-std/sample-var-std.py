import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    n = np.size(x)
    total = 0

    for i in x:
        total += (i - mean) ** 2

    var = float(total / (n - 1))
    std = float(np.sqrt(var))
    
    return {"variance":var, "standard_deviation":std}