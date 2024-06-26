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

    CREATE TABLE Gym
    (
    GymID INT PRIMARY KEY AUTO_INCREMENT,
    GymName VARCHAR(255) NOT NULL
    );

    CREATE TABLE Machine_table
    (
    MachineID INT PRIMARY KEY AUTO_INCREMENT,
    GymID INT NOT NULL,
    foreign key (GymID) references Gym(GymID),
    Machine_name VARCHAR(255) NOT NULL,
    Installment_date DATE NOT NULL,
    Wear_tear_index INT
    );

    CREATE TABLE Exercise_score_table
    (
    Exercise VARCHAR(255) NOT NULL,
    MemberID INT NOT NULL,
    foreign key (MemberID) references Member_table(MemberID),
    High_score INT
    );

    CREATE TABLE Machine_stats_table
    (
    MachineID INT NOT NULL,
    foreign key (MachineID) references Machine_table(MachineID),
    MemberID INT NOT NULL,
    foreign key (MemberID) references Member_table(MemberID),
    Total_rep_count INT,
    High_score INT
    );
"""

using_db = """USE statistical_database_for_gym;"""

insert_member = """INSERT INTO Member_table(Member_Fname,Member_Lname,Date_Of_birth,Weight,Height)
VALUES
"""

insert_gym = """INSERT INTO Gym(GymName)
VALUES
"""

insert_exercise_score = """INSERT INTO Exercise_score_table(Exercise, MemberID, High_score)
VALUES
"""

insert_machine = """INSERT INTO Machine_table(GymID ,Machine_name, Installment_date)
VALUES
"""
