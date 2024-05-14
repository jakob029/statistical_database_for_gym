"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import random
import json
import datetime
from data_generation.src.data_name_parcer import DataNameParcer
from data_generation.statistical_models import tools


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

def generate_date(start_years_ago: int, end_years_ago: int) -> str:
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    this_year = datetime.datetime.now().year
    year = random.randint(this_year-start_years_ago, this_year-end_years_ago)
    month = random.randint(1, 12)
    day = random.randint(1, days_in_month[month-1])

    return f'{year}-{month}-{day}'
