"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import random
from datetime import datetime, date
from data_generation.src import exceptions
from data_generation.src.data_name_parcer import DataNameParcer
from data_generation.src.generator_functions import (
    generate_name_from_parcer,
    generate_statistics_based_value,
)
from data_generation.src import paths
from data_generation.statistical_models import tools

PARCEDL = DataNameParcer(paths.NAME_LAST)
PARCEDM = DataNameParcer(paths.NAME_MAN)
PARCEDW = DataNameParcer(paths.NAME_WOMAN)


class GymMember:
    """Structure class for a gym member."""

    member_id: int

    gender: int
    birthday: str
    first_name: str
    last_name: str
    date_of_birth: str

    weight: int
    height: int

    exercises: tuple = {}

    def __init__(
        self,
        gender: int = None,
        fist_name: str = None,
        last_name: str = None,
        birthday: str = None,
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

        if not birthday:
            self.generate_data_of_birth()

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

    def setup_personal_stats(self):
        """Set up the weight, length and exercise statistic for the person
        based on standard distributed statistical data.
        """
        self._setup_weight()
        self._setup_length()

        strength_standard_deviation_age = tools.generate_standardized_value(0, 1)
        strength_standard_deviation_bw = tools.generate_standardized_value(0, 1)
        for lift in ["bench-press", "squat", "deadlift"]:
            self._setup_lifts(
                lift, strength_standard_deviation_age, strength_standard_deviation_bw
            )

    def _setup_weight(self):
        section_tuple = ("Men weight", "Woman weight")
        mean, sigma = generate_statistics_based_value(
            self.get_age(), paths.WEIGHT_FUNCTIONS, [section_tuple[self.gender]]
        )

        self.weight = tools.generate_standardized_value(mean, sigma)

    def _setup_length(self):
        section_tuple = ("Men length", "Woman length")
        mean, sigma = generate_statistics_based_value(
            self.get_age(), paths.LENGTH_FUNCTIONS, [section_tuple[self.gender]]
        )

        self.height = tools.generate_standardized_value(mean, sigma)

    def _setup_lifts(self, lift, strength_sigma_age, strength_sigma_weight):
        bw_section_tuple = ("Men bodyweight", "Female bodyweight")
        age_section_tuple = ("Men age", "Female age")

        bw_mean, bw_sigma = generate_statistics_based_value(
            self.get_age(),
            paths.EXERCISE_WEIGHT_FUNCTIONS,
            [lift, bw_section_tuple[self.gender]],
        )
        age_mean, age_sigma = generate_statistics_based_value(
            self.get_age(),
            paths.EXERCISE_WEIGHT_FUNCTIONS,
            [lift, age_section_tuple[self.gender]],
        )

        applied_deviation_bw = strength_sigma_weight + random.randint(-5, 5) / 10
        applied_deviation_age = strength_sigma_age + random.randint(-5, 5) / 10

        bw_value = bw_mean + applied_deviation_bw * bw_sigma
        age_value = age_mean + applied_deviation_age * age_sigma

        self.exercises[lift] = (bw_value + age_value) / 2

    def get_structured_output(self) -> str:
        """Generate a output print with values to feed the database."""
        return f"'{self.first_name}', '{self.last_name}', '{self.birthday}', {int(round(self.weight))}, {int(round(self.height))}"

    def generate_data_of_birth(self):
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        this_year = datetime.now().year
        birth_year = random.randint(this_year-90, this_year-16)
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, days_in_month[birth_month-1])

        self.birthday = f'{birth_year}-{birth_month}-{birth_day}'

    def get_age(self) -> int:
        today = date.today()
        born_day = datetime.strptime(self.birthday, '%Y-%m-%d')
        return today.year - born_day.year - ((today.month, today.day) < (born_day.month, born_day.day))
