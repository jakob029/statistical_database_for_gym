"""Layout:
- Insert a member set on machine into Machine stats table.
- Insert a member that does an exercise
"""

mysql_stored_procedures = """
CREATE PROCEDURE InsertSet (IN MachID int, IN MemID int, IN Reps INT, IN Weight INT)
BEGIN
    DECLARE new_score INT;
    SET new_score = round(Weight / EXP(-0.023 * (Reps - 1)));

    if (Select count(*) from Machine_stats_table where
    MachID = MachineID and MemID = MemberID) > 0
    THEN
        UPDATE Machine_stats_table SET High_score = GREATEST(High_score, new_score)
        where MachID = MachineID and MemID = MemberID;

        UPDATE Machine_stats_table SET Total_rep_count = Total_rep_count + Reps
        where MachID = MachineID and MemID = MemberID;
    ELSE
        INSERT INTO Machine_stats_table(MachineID, MemberID, Total_rep_count, High_score)
        VALUES (MachID, MemID, Reps, new_score);
    END IF;
END;
"""
