# measurepy
A python module to boost first-step data analysis after measurements.

## Problem and Motivation

It is very complicated and tedious to deal with data in my physics lab course. Hence, I develop such a package to boost the process. After the first-step analysis, you can turn to complicated and advanced tools or just finish the report if the experiment is simple.

## Features

- [x] Directly get the value and error with multi-measurements.
- [x] Simple linear regession (based on scipy now).
- [ ] Simple plotting with just a parameter to choose the style.
- [ ] Plus, minus, multiply, divide with errors.

## Installation

With `pip3`, just type

    pip3 install measurepy


## Usage

For the multimeasure feature,

    import numpy as np
    from measurepy.multimeasure import *

    A = np.array([1, 2, 3, 4, 5])
    mean, delta_a, error = cal_error(A, 0.01)
    print(mean)
    print(delta_a)
    print(error)

For linear regression,

    import numpy as np
    from measurepy.regression import *

    x = np.array([1, 2, 3, 4, 5])
    y = np.array(x**2 + 1)
    slope, intercept, slope_err, intercept_err, rsquare = lineareg(x, y)
