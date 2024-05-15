"""Layout:
- Insert a member set on machine into Machine stats table.
- Insert a member that does an exercise
"""

stored_procedures = """
delimiter //

CREATE PROCEDURE InsertSet (IN MachineID int, IN MemberID int, IN Reps INT, IN Weight INT)
BEGIN
    DECLARE find_row INT;
    Select count(*) into find_row from Machine_stats_table where
    MachineID = MachineID and MemberID = MemberID;

    DECLARE new_score INT;
    SET new_score = round(EXP(-0.023 * (Reps - 1)) * Weight);

    if find_row > 0
    THEN
        UPDATE Machine_stats_table SET Highscore = GREATEST(Highscore, new_score)
        where MachineID = MachineID and MemberID = MemberID;
    ELSE
        INSERT INTO Machine_stats_table(MachineID, MemberID, Total_rep_count, Highscore)
        VALUES (MachineID, MemberID, Reps, new_score);
    ENDIF;
END //

DELIMITER ;
"""
