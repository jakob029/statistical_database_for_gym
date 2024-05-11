"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import random
import json
from data_name_parcer import DataNameParcer
from statistical_models import tools


def generate_name_from_parcer(parced_data_object: DataNameParcer):
    """Generate random name based on parced data.
    Args:
        ParcedDataObject: An object with parced data.
    Returns:
        A completely random name based on the data.
        (This shall be updated to statistics based)
    """
    name_dict = parced_data_object.generate_name_dict()
    return random.choice(list(name_dict.items()))[1].title()


def generate_statistics_based_value(
    x_value, stat_file_path: str, recourse_path: list
) -> tuple:
    """Get the value based on mean and standard deviation functions for a given x value.
    Args:
        x_value: The x value (e.g age or weight) for wanted value
        stat_file_path: Path to the stats function file wanted.
        recourse: Recourse in the file wanted.
    Returns:
        A tuple with (Mean, standard deviation).
    """
    with open(stat_file_path, mode="r", encoding="utf-8") as stat_file:
        constant_dict = json.load(stat_file)

        for path in recourse_path:
            constant_dict = constant_dict[path]

        return tools.polynomial_function(
            x_value, *constant_dict["mean"]
        ), tools.polynomial_function(x_value, *constant_dict["sigma"])
