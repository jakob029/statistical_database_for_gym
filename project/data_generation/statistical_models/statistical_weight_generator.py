"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import json
import purpose_built_models.source_training_data as data
import tools


def generate_math_functions(exercises: list = None) -> None:
    """Generate a file that contains all variables that create the polynomial function that
    defines a specific case."""
    json_dict = {}

    if not exercises:
        exercises = ["bench-press", "squat", "deadlift"]
    table_types = ["Men bodyweight", "Men age", "Female bodyweight", "Female age"]

    for exercise in exercises:
        training_data = data.get_structured_training_data(exercise)
        json_dict[exercise] = {}
        for table_type in table_types:
            average_per_class = data.get_average_per_class(table_type, training_data)

            generated_mean_function = tools.fit_function_to_cordinates(
                average_per_class
            )
            generated_sigma_function = tools.fit_function_to_cordinates(
                average_per_class, 1
            )

            json_dict[exercise][table_type] = {
                "mean": generated_mean_function,
                "sigma": generated_sigma_function,
            }

    with open(
        "project/data_generation/schemas/exercise_weight_functions.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(json_dict, file, indent=4)
