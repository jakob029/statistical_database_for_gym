from build_database.src.data_base_handler import DataBaseHandler
from data_generation import generate_member, generate_machine

def run():
    init_db = DataBaseHandler()
    init_db.insert_user_generated_data(generate_member.GymMember, 20)
    init_db.insert_gym_machines(generate_machine.get_structured_machine_output, 12)

if __name__ == "__main__":
    run()
