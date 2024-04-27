"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import random
from data_name_parcer import DataNameParcer


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
