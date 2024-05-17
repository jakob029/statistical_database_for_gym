"""Layout:
- Get the total number of reps a member has done across all machines.
- Get the total number of reps done in total.
- Get a "wear and tear" index of 1 - 10, calculated from installment date and num of reps.
"""

total_number_reps = """
DELIMITER //

CREATE FUNCTION total_num_reps()
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE total_reps INT;
    SELECT SUM(Total_rep_count) INTO total_reps FROM Machine_stats_table;
    RETURN total_reps;
END //

DELIMITER ;
"""

member_total_reps = """
DELIMITER //

CREATE FUNCTION member_total_reps(inMemberID INT)
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE member_reps INT;
    SELECT SUM(Total_rep_count) INTO member_reps FROM Machine_stats_table where inMemberID = MemberID;
    RETURN member_reps;
END //

DELIMITER ;
"""

machine_total_reps = """
DELIMITER //

CREATE FUNCTION member_total_reps(inMachineID INT)
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE machine_reps INT;
    SELECT SUM(Total_rep_count) INTO member_reps FROM Machine_stats_table where inMachineID = MachineID;
    RETURN machine_reps;
END //

DELIMITER ;
"""