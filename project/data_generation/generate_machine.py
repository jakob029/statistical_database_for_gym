from data_generation.src import paths
import random
from data_generation.src.generator_functions import generate_date

def generate_machine(gym_open_years: int) -> tuple:
    """Generate a new machine based on names in some schemas/gym_machines.data

    Returns:
        (Machine name, Installment date)
    """
    with open(paths.GYM_MACHINES, 'r', encoding='utf-8') as file:
        machine_names = file.read().splitlines()
        return random.choice(machine_names), generate_date(gym_open_years, 0)

def get_structured_machine_output(GymID: int, gym_open_years: int = 10) -> str:
    """Generate structured insert values for a gym_machine.
    Args:
        gym_open_years: Number of years the gym has been open.
    Returns:
        A string following the insert structure of
        (GymID, Machine_name, Installment_date)
        """

    m_name, ins_date = generate_machine(gym_open_years)
    return f"{GymID}, '{m_name}', '{ins_date}'"
