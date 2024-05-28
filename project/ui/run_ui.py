import os
import time
def run_ui() -> tuple:
    func_args = []
    os.system("cls || clear")

    func_proc_dict = {"1": [], "2": ["MemberID"], "3":["inMachineID"],
                      "4": ["MachineID"], "5": ["Exercise (bench-press, squat or deadlift)"],
                      "6": ["MachineID", "MemberID", "Reps", "Weight"],
                      "7": ["exercise (bench-press, squat or deadlift)", "MemID", "Reps", "Weight"]}

    funcs = ["total_num_reps", "member_total_reps", "machine_total_reps", "Get_Highscore_machine",
             "Highscore_exercise", "insert_machine_set", "insert_exercise_set"]
    while True:
        print("Welcome!\n")
        print("Select a number from below the functions listed below:\n")
        print("1: total_num_reps")
        print("2: member_total_reps")
        print("3: machine_total_reps")
        print("4: Get_Highscore_machine")
        print("5: Highscore_exercise")
        print("Or procedure:")
        print("6: insert_machine_set")
        print("7: insert_exercise_set")

        user_input = input()
        if user_input < '1' or user_input > '7':
            print("\nPlease select a number!")
            time.sleep(1.5)
            os.system("cls || clear")
            continue
        break
    
    func_args.append(user_input < "6")
    func_args.append(funcs[int(user_input)-1])
    for arg in func_proc_dict[user_input]:
        func_args.append(
            input(f'{arg}: ')
        )

    return func_args