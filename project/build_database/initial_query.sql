CREATE DATABASE statistical_database_for_gym;
USE statistical_database_for_gym;

CREATE TABLE Member_table
(
MemberID INT PRIMARY KEY AUTO_INCREMENT,
Member_name VARCHAR(255) NOT NULL,
Date_Of_birth DATE NOT NULL,
Signup_date DATE NOT NULL,
Weight INT,
Height INT
);

CREATE TABLE Machine_table
(
MachineID INT PRIMARY KEY AUTO_INCREMENT,
Machine_name VARCHAR(255) NOT NULL,
Installment_date DATE NOT NULL,
Total_numer_of_reps INT,
Highscore INT
);

CREATE TABLE Exercise_score_table
(
Exercuse VARCHAR(255) NOT NULL,
MemberID INT NOT NULL,
Highscore INT
);

CREATE TABLE Machine_stats_table
(
MachineID INT NOT NULL,
MembereID INT NOT NULL,
Total_rep_count INT,
Highscore INT
);
