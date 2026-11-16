import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    arr = np.asarray(x, dtype=float)
    res = 1.0 / (1.0 + np.exp(-arr))
    return float(res) if np.isscalar(x) else res
        