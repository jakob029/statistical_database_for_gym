### Architecture


#### Member table
|MemberID (PK)|Member Fname|Member Lname|Date Of Birth|Sign-up date|Weight|Height|
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |

#### Machine table
|MachineID (PK)|Machine name|Installment Date|Total number of reps|Highscore|
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

### Protental Architecture changes

 - The tables shall be normalized in line with 3NF.


### 1rp max calculation estimate
 - <percentage of max = 100 * e^(-0.023 * (reps-1))>
 - Estimates per median weight and standard deviation can be calculated in the python data generation code.

### Instructions
    To generate a member, initiate a GymMember instance from project/data_generation/main.py


### Start using program
    #### On a linux based system:

    To begin using this program, first make sure a mySQL server is installed and active:
    Install guide:
        $sudo apt update
        $sudo apt install mysql-server
        (Check that it is using by running)
            $sudo mysql

    Then create a user by doing:
        CREATE USER '<SET_USERNAME>'@'localhost' IDENTIFIED BY '<PASSWORD>';
    Grant permissions to user:
        GRANT ALL PRIVILEGES ON *.* TO '<USERNAME>'@'localhost';
