"""This project is a part of Blekinge institute of technology's 
assignment all code is developed by jakob029 & FilipDar."""
from build_database.src.data_base_handler import DataBaseHandler
from data_generation import generate_member, generate_machine
from ui.run_ui import run_ui

HOST = "localhost"


def run():
    """Generate a database with tables, functions, stored procedures, triggers and data."""
    init_db = DataBaseHandler(HOST)
    if not init_db.database_exists():
        init_db.build_database()
        init_db.insert_new_gym("Karlskrona", "Lund", "Höllviken")
        init_db.insert_user_generated_data(generate_member.GymMember, 500)
        init_db.insert_gym_machines(generate_machine.get_structured_machine_output, 5, 1)
        init_db.insert_gym_machines(generate_machine.get_structured_machine_output, 5, 2)
        init_db.insert_gym_machines(generate_machine.get_structured_machine_output, 5, 3)

    while True:
        do_exe = run_ui()
        if do_exe[0]:
            init_db.execute_function(do_exe)
        else:
            init_db.execute_procedure(do_exe)

if __name__ == "__main__":
    run()
