import time
import mysql
from typing import Callable
from mysql.connector import connect, Error
import getpass
import build_database.src.mysql_queries as q


class DataBaseHandler:

    USERNAME: str
    PASSWORD: str
    DATABASE_CONNECTION: mysql.connector.connection_cext.CMySQLConnection
    CURSOR: mysql.connector.cursor_cext.CMySQLCursor

    def __init__(self) -> None:
        self.USERNAME = input("Enter username: ")
        self.PASSWORD = getpass.getpass("Password: ")
        self._initiate_database()
        self._build_database_base()

    def _initiate_database(self) -> None:
        try:
            self.DATABASE_CONNECTION = connect(
                host="jefd2024.mysql.database.azure.com",
                user=self.USERNAME,
                password=self.PASSWORD,
            )
            self.CURSOR = self.DATABASE_CONNECTION.cursor()
        except Error:
            print("Could not connect to database!")
            raise Error

    def _build_database_base(self):
        query = self._get_build_query()
        self.CURSOR.execute(query)
        self.CURSOR.close()
        print("Database created!")

    def insert_user_generated_data(
        self, member_generator: Callable[..., str], num_of_members: int
    ):
        for i in range(num_of_members):
            self._initiate_database()
            new_member = member_generator()
            new_member.setup_personal_stats()
            mem_query = (
                f"{q.insert_member}({new_member.get_structured_output()}); COMMIT;"
            )

            additional_query = ""
            for exercise, weight in new_member.exercises.items():
                additional_query += f"{q.insert_exercise_score} ('{exercise}', {1000+i}, {weight}); COMMIT;"

            query = mem_query + additional_query
            time.sleep(0.05)
            self.CURSOR.execute(q.using_db)
            self.CURSOR.execute(query)
            self.CURSOR.close()

        print(f"Added {num_of_members} new autogenerated members!")

    def insert_gym_machines(
        self, machine_generator: Callable[..., str], num_of_machines: int, gymID
    ):
        for _ in range(num_of_machines):
            self._initiate_database()

            machine_query = f"{q.insert_machine}({machine_generator(gymID)}); COMMIT;"
            time.sleep(0.05)
            self.CURSOR.execute(q.using_db)
            self.CURSOR.execute(machine_query)
            self.CURSOR.close()
        print(f"Added {num_of_machines} new autogenerated members!")

    def insert_new_gym(self, *locations):
        for location in locations:
            time.sleep(0.05)
            self._initiate_database()
            self.CURSOR.execute(q.using_db)
            self.CURSOR.execute(f"{q.insert_gym}('{location}'); COMMIT;")
            self.CURSOR.close()

    @staticmethod
    def _get_build_query() -> str:
        return q.build_query
