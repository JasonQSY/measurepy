# measurepy
A python module to boost first-step data analysis after measurements.

## Problem and Motivation

It is very complicated and tedious to deal with data in my physics lab course. Hence, I develop such a package to boost the process. After the first-step analysis, you can turn to complicated and advanced tools or just finish the report if the experiment is simple.

## Features

- [x] Directly get the value and error with multi-measurements.
- [ ] Simple linear regession.
- [ ] Simple plotting with just a parameter to choose the style.
- [ ] Plus, minus, multiply, divide with errors.

## Installation

The package has not been published to `pip` although I aim to do so. Currently, you can install it by running

    git clone https://github.com/JasonQSY/measurepy && cd measurepy
    pip3 install .


## Usage

For the multimeasure feature,

    import numpy as np
    from measurepy.multimeasure import *

    A = np.array([1, 2, 3, 4, 5])
    mean, delta_a, error = cal_error(A, 0.01)
    print(mean)
    print(delta_a)
    print(error)
