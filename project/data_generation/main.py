import random
import exceptions
from data_name_parcer import DataNameParcer
from generator_functions import generate_name_from_parcer
from paths import name_last, name_man, name_woman

PARCEDL = DataNameParcer(name_last)
PARCEDM = DataNameParcer(name_man)
PARCEDW = DataNameParcer(name_woman)


class GymMember:
    gender: int
    first_name: str
    last_name: str
    date_of_birth: str

    def generate_gym_member(self, gender = None, fist_name = None, last_name = None):
        self.gender = gender
        if not gender:
            self.gender = random.randint(0,1)

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
        print(f'Your new members name is {self.first_name} {self.last_name}')

if __name__ == "__main__":
    new_member = GymMember()
    new_member.generate_gym_member()
