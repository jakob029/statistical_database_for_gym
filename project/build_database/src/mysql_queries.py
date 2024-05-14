build_query = """
    CREATE DATABASE statistical_database_for_gym;
    Use statistical_database_for_gym;

    CREATE TABLE Member_table(
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    Member_Fname VARCHAR(255) NOT NULL,
    Member_Lname VARCHAR(255) NOT NULL,
    Date_Of_birth DATE,
    Weight INT,
    Height INT
    ) AUTO_INCREMENT = 1000;

    CREATE TABLE Machine_table
    (
    MachineID INT PRIMARY KEY AUTO_INCREMENT,
    Machine_name VARCHAR(255) NOT NULL,
    Installment_date DATE NOT NULL,
    Total_number_of_reps INT,
    Highscore INT
    );

    CREATE TABLE Exercise_score_table
    (
    Exercise VARCHAR(255) NOT NULL,
    MemberID INT NOT NULL,
    foreign key (MemberID) references Member_table(MemberID),
    Highscore INT
    );

    CREATE TABLE Machine_stats_table
    (
    MachineID INT NOT NULL,
    foreign key (MachineID) references Machine_table(MachineID),
    MemberID INT NOT NULL,
    foreign key (MemberID) references Member_table(MemberID),
    Total_rep_count INT,
    Highscore INT
    );
"""

using_db = """USE statistical_database_for_gym;"""

insert_member = """INSERT INTO Member_table(Member_Fname,Member_Lname,Date_Of_birth,Weight,Height)
VALUES
"""

insert_exercise_score = """INSERT INTO Exercise_score_table(Exercise, MemberID, Highscore)
VALUES
"""

insert_machine = """INSERT INTO Machine_table(Machine_name, Installment_date, Total_number_of_reps, Highscore)
VALUES
"""
