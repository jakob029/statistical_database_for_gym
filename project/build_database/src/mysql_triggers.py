"""Layout.
- Instead update wear and tear score.
"""

SQL_Triggers = """
CREATE TRIGGER update_wear_and_tear AFTER UPDATE ON machine_stats_table
FOR EACH ROW
    BEGIN
        update machine_table
        SET Wear_tear_index = (new.Total_rep_count / 100 + DATEDIFF(CURDATE(),installment_date)) / 1000
        WHERE MachineID = NEW.MachineID;
    end $$
"""
