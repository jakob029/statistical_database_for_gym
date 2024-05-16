"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import numpy as np
from scipy.optimize import curve_fit


def third_degree_function(x: int, a: int, b: int, c: int, d: int) -> int:
    """Sixth degree function calculator."""
    return a * x**3 + b * x**2 + c * x + d


def polynomial_function(x: int, *degree_constants: list) -> float:
    """Get a value based on some mathematical polynomial function and an x value.
    Args:
        x: The x value for the y value wanted.
        degree_constants: Each constant for the polynomial function in
          descending order (based on x exponent).
    Returns:
        Curve y value.
    """
    degree_constants = list(degree_constants)
    degree_constants.reverse()
    value = 0
    for i, constant in enumerate(degree_constants[1:]):
        value += constant * x ** (i + 1)
    value += degree_constants[0]
    return value


def fit_function_to_cordinates(cordinate_values: int, mean_or_sigma: int = 0) -> tuple:
    """Generate a mathematical function based on some input coordinates.
    Args:
        cordinate_values: List of tuples with coordinate values.
        mean_or_sigma: Give 0 for mean and 1 for standard deviation.
    """
    x_values = np.array([value[0] for value in cordinate_values])
    y_values = np.array([value[1 + mean_or_sigma] for value in cordinate_values])

    params = curve_fit(third_degree_function, x_values, y_values)
    [a, b, c, d] = params[0]

    return a, b, c, d


def generate_standardized_value(mean: float, sigma: float, down_cap: float = None) -> float:
    """Generate a randomized value where the probability follows a standard deviation curve.
    Args:
        Mean: The mean of the sample.
        Sigma: The standard deviation of the sample
        down_cap: Minimum returnable value
    Returns:
        Random value based on standard deviation (Gaussian distribution).
    """
    if not down_cap:
        return np.random.normal(mean, sigma)
    generated_value = -10
    while generated_value < down_cap:
        generated_value = np.random.normal(mean, sigma)
    return generated_value
