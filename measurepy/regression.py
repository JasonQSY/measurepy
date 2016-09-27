import numpy as np
from scipy.stats import linregress

def lineareg(x, y):
    """Apply linear regression for a numpy array.

    Args:
        x(numpy.array): x.
        y(numpy.array): y.

    Returns:
        slope(float): the estimated value of slope.
        intercept(float): the estimated value of intercept on y axis.
        slope_err(float): the std-error of slope.
        intercept_err(float): the std-error of intercept.
        rsquare(float): $R^2$ for rvalue. It is close to 1 if the relationship is linear.
    """
    slope, intercept, rvalue, pvalue, slope_err = linregress(x, y)
    intercept_err = (np.mean(x**2)**0.5) * slope_err
    rsquare = rvalue**2
    return slope, intercept, slope_err, intercept_err, rsquare
