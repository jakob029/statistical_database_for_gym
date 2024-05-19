### Architecture


#### Member table
|MemberID (PK)|Member Fname|Member Lname|Date Of Birth|Sign-up date|Weight|Height|
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |

#### Gym table
|GymID (PK)|Gym name|
|---|---|
|   |   |
|   |   |
|   |   |

#### Machine table
|MachineID (PK)|GymID (FK)|Machine name|Installment Date|Wear and tear index|
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

#### Exercise score table
|Exercise|MemberID (FK)|Highscore|
|---|---|---|
|Running 5k|   |   |
|Running 10k|   |   |
|Bench press|   |   |
|Squat|   |   |
|Deadlift|   |   |


#### Machine stats table
|MachineID (FK)|MemberID (FK)|Total rep count|1rp max indicator|
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

### Start using program
    #### On a linux based system:

    To begin using this program, first make sure a mySQL server is installed and active:
    Install guide:
        $sudo apt update
        $sudo apt install mysql-server
        (Check that it is using by running)
            $sudo mysql

    Then create a user by doing:
        $sudo service mysql start
        $mysql -u root mysql
        CREATE USER '<SET_USERNAME>'@'localhost' IDENTIFIED BY '<PASSWORD>';
    Grant permissions to user:
        GRANT ALL PRIVILEGES ON *.* TO '<USERNAME>'@'localhost';

    Specify you location in project/main.py (default is localhost)

    Generate a venv environment and install requirements:
        $python3 -m venv <ENVIRONMENT NAME>
        $source <ENVIRONMENT NAME>/bin/activate

    Run the program:
        $python3 project/main.py

    Then write your username and password.

    A database will now be created in your specified location.

### Instructions
    When running the program, a database will automatically be generated.

    When a member has preformed a new set on a machine, use:
        $CALL insert_machine_set((<MachID>, <MemID>,<Reps>, <Weight>))

    When a member has preformed a new exercise set, use:
        $CALL insert_exercise_set (<exercise>, <MemID>, <Reps>, <Weight>)

    A trigger will automatically update the Wear_tear_index when adding new set is inserted.

### Available MySQL utilities
    All utilities will automatically be loaded into the database when running the python program.

    Functions:
    - total_num_reps ()
    - member_total_reps (inMemberID)
    - machine_total_reps (inMachineID)
    - Get_Highscore_machine (MachineID)
    - Highscore_exercise (Exercise name)
    Procedures:
    - insert_machine_set (MachID,MemID,Reps,Weight)
    - insert_exercise_set (exercise, MemID, Reps, Weight)


### 1rp max calculation estimate
 - <percentage of max = 100 * e^(-0.023 * (reps-1))>
 - Estimates per median weight and standard deviation can be calculated in the python data generation code.
