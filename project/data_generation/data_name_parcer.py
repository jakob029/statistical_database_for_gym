"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""

import re
import yaml


class DataNameParcer:
    """File for pacing Swedish SCB name statistics."""

    NAME_STAT_LIST: list

    class NameStat:
        """Person structure class."""

        def __init__(self, rank: int, name: str, no_count: int) -> None:
            """Constructor."""
            self.rank = rank
            self.name = name
            self.no_count = no_count

    def __init__(self, file_path: str) -> None:
        """Constructor."""
        self.NAME_STAT_LIST = []
        with open(file_path, "r", encoding="utf-8") as n_file:
            line = n_file.readline()
            while line:
                spl = re.split(r"\t", line)
                no_count = int(spl[2].replace(" ", ""))
                self.NAME_STAT_LIST.append(self.NameStat(int(spl[0]), spl[1], no_count))
                line = n_file.readline()

    def get_person_list(self) -> tuple:
        """Get a list names."""
        return tuple(self.NAME_STAT_LIST)

    def generate_yaml_file(self, file_name: str):
        """Generate a YAML file based on the statistics.
        Args:
            file_name: Path to file.
        """
        write_dict = {}
        for element in self.NAME_STAT_LIST:
            write_dict[element.rank] = element.name

        with open(file_name, "w", encoding="utf-8") as file:
            yaml.dump(write_dict, file)

    def generate_name_dict(self):
        """Generate and return a dictionary of names and ranks
        Returns:
            Dict with structure {rank: name}
        """
        name_dict = {}
        for element in self.NAME_STAT_LIST:
            name_dict[element.rank] = element.name

        return name_dict
