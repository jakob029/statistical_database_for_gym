"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import random
import exceptions
from data_name_parcer import DataNameParcer
from generator_functions import generate_name_from_parcer
from paths import NAME_LAST, NAME_MAN, NAME_WOMAN

PARCEDL = DataNameParcer(NAME_LAST)
PARCEDM = DataNameParcer(NAME_MAN)
PARCEDW = DataNameParcer(NAME_WOMAN)


class GymMember:
    """Structure class for a gym member."""

    gender: int
    first_name: str
    last_name: str
    date_of_birth: str

    def generate_gym_member(
        self, gender: int = None, fist_name: str = None, last_name: str = None
    ):
        """Generate a new Gym member, if custom name or gener is wanted, input args.
        Args:
            gender: 0 for male, 1 for female.
            fist_name: Any first name (must be combined with last_name)
            last_name: Any last name (must be combined with first_name)
        """
        self.gender = gender
        if not gender:
            self.gender = random.randint(0, 1)

        if fist_name and last_name:
            return

        if fist_name or last_name:
            raise exceptions.InputNameError

        match self.gender:
            case 0:
                self.first_name = generate_name_from_parcer(PARCEDM)
                self.last_name = generate_name_from_parcer(PARCEDL)
            case 1:
                self.first_name = generate_name_from_parcer(PARCEDW)
                self.last_name = generate_name_from_parcer(PARCEDL)
