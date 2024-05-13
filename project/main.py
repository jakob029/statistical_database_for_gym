from build_database.src.data_base_handler import DataBaseHandler
from data_generation import generate_member

def run():
    init_db = DataBaseHandler()
    init_db.insert_user_generated_data(generate_member.GymMember, 200)

if __name__ == "__main__":
    run()
