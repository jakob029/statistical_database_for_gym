"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import numpy as np
from scipy.optimize import curve_fit


def sextic_equation(
    x: int, a: int, b: int, c: int, d: int, e: int, f: int, g: int
) -> int:
    """Sixth degree function calculator."""
    return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g


def fit_function_to_cordinates(cordinate_values: int):
    """Generate a mathimatical function based on some input cordinations."""
    x_values = np.array([value[0] for value in cordinate_values])
    y_values = np.array([value[1] for value in cordinate_values])

    params = curve_fit(sextic_equation, x_values, y_values)
    [a, b, c, d, e, f, g] = params[0]

    return a, b, c, d, e, f, g


"""Showcase of how to use model below.

import purpose_built_models.source_training_data as data

training_data = data.get_structured_training_data("bench-press")
average_training_bench = data.get_average_per_class("Men age", training_data)
generated_function = fit_function_to_cordinates(average_training_bench)

average lift = sextic_equation(<age or bodyweight>, *generated_function)
"""
