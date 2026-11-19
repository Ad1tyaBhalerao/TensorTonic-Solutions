import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x, dtype=float)
    
    total = ((x - np.mean(x)) ** 2).sum()
    n = np.size(x)

    var = float(total / (n - 1))
    std = float(np.sqrt(var))
    
    return {"variance":var, "standard_deviation":std}