"""Layout:
- Get the total number of reps a member has done across all machines.
- Get the total number of reps done in total.
"""

mysql_functions = """
CREATE FUNCTION total_num_reps()
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE total_reps INT;
    SELECT SUM(Total_rep_count) INTO total_reps FROM Machine_stats_table;
    RETURN total_reps;
END;


CREATE FUNCTION member_total_reps(inMemberID INT)
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE member_reps INT;
    SELECT SUM(Total_rep_count) INTO member_reps FROM Machine_stats_table where inMemberID = MemberID;
    RETURN member_reps;
END;

CREATE FUNCTION member_total_reps(inMachineID INT)
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE machine_reps INT;
    SELECT SUM(Total_rep_count) INTO member_reps FROM Machine_stats_table where inMachineID = MachineID;
    RETURN machine_reps;
END;


CREATE FUNCTION Get_Highscore_machine(MachineID INT) RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(255);
    SELECT CONCAT('Name: ', m.Member_Fname, ' ', m.Member_Lname,
                  ', Gym name: ', g.GymName,
                  ', Machine name: ', ma.Machine_name,
                  ', Highscore: ', MAX(ms.Highscore)) INTO result
    FROM Machine_stats_table ms
    JOIN Member_table m ON ms.MemberID = m.MemberID
    JOIN Machine_table ma ON ms.MachineID = ma.MachineID
    JOIN Gym g ON ma.GymID = g.GymID
    WHERE ma.MachineID = MachineID
    GROUP BY m.Member_Fname, m.Member_Lname, g.GymName, ma.Machine_name
    ORDER BY MAX(ms.Highscore) DESC
    LIMIT 1;

    RETURN result;
END;

CREATE FUNCTION Highscore_exercise(Exercise VARCHAR(255)) RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(255);
    SELECT CONCAT('Name: ', m.Member_Fname, ' ', m.Member_Lname,
                  ', Exercise: ', e.Exercise,
                  ', Highscore: ', MAX(e.Highscore)) INTO result
    FROM exercise_score_table e
    JOIN Member_table m ON e.MemberID = m.MemberID
    WHERE e.Exercise = Exercise
    GROUP BY m.Member_Fname, m.Member_Lname, e.Exercise
    ORDER BY MAX(e.Highscore) DESC
    LIMIT 1;

    RETURN result;
END;
"""
