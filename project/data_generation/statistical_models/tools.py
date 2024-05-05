"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import numpy as np
from scipy.optimize import curve_fit


def sextic_equation(
    x: int, a: int, b: int, c: int, d: int
) -> int:
    """Sixth degree function calculator."""
    return a * x**3 + b * x**2 + c * x + d

def fit_function_to_cordinates(cordinate_values: int, mean_or_sigma: int = 0) -> tuple:
    """Generate a mathimatical function based on some input cordinations.
    Args;
        cordinate_values: List of tuples with cordinate values.
        mean_or_sigma: Give 0 for mean and 1 for standard deviation.
    """
    x_values = np.array([value[0] for value in cordinate_values])
    y_values = np.array([value[1 + mean_or_sigma] for value in cordinate_values])

    params = curve_fit(sextic_equation, x_values, y_values)
    [a, b, c, d] = params[0]

    return a, b, c, d
