import numpy as np

def cal_error(array, typeb = 0):
    """Calculate all errors of the input array.

    Args:
        array (numpy.array): The data measured directly for a single
            physical datus. We use the mean value as the reliable
            measurement for that and get type-A error meanwhile.
        typeb (float): The type-B error collected directly from the
            instrucments.

    Returns:
        mean (float): The mean value of the array.
        delta_a (float): The type-A error of the array.
        error (float): The merged error of type-A and type-B

    """
    size = array.size
    mean = array.mean()
    std = array.std(ddof = 1)
    params = {
        3: 2.48,
        4: 1.59,
        5: 1.204,
        6: 1.05,
        7: 0.926,
        8: 0.834,
        9: 0.770,
        10: 0.715
    }
    delta_a = std * params[size]

    if typeb == 0:
        return mean, delta_a

    deltb_b = typeb
    error = (delta_a**2 + deltb_b**2) ** 0.5
    return mean, delta_a, deltb_b
