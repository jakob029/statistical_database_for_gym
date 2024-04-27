import re
import yaml

class DataNameParcer:
    """File for parcing Swedish SCB name statistics."""
    PERSON_LIST: list
    class Person:
        """Person structure class."""
        def __init__(self, rank: int, name: str, no_count: int) -> None:
            self.rank = rank
            self.name = name
            self.no_count = no_count

    def __init__(self, file_path: str) -> None:
        """Constructor"""
        self.PERSON_LIST = []
        with open(file_path, 'r', encoding = 'utf-8') as n_file:
            line = n_file.readline()
            while line:
                spl = (re.split(r'\t', line))
                no_count = int(spl[2].replace(' ', ''))
                self.PERSON_LIST.append(self.Person(int(spl[0]), spl[1], no_count))
                line = n_file.readline()

    @staticmethod
    def get_person_list(self) -> tuple:
        return tuple(self.PERSON_LIST)

    def generate_yaml_file(self, file_name: str):
        write_dict = {}
        for element in self.PERSON_LIST:
            write_dict[element.rank] = element.name

        with open(file_name, 'w', encoding='utf-8') as file:
            yaml.dump(write_dict, file)

    @staticmethod
    def generate_name_dict(self):
        name_dict = {}
        for element in self.PERSON_LIST:
            name_dict[element.rank] = element.name

        return name_dict
