"""Layout.
- Instead update wear and tear score.
"""

mysql_triggers = """
CREATE TRIGGER update_wear_and_tear AFTER INSERT ON Machine_stats_table
FOR EACH ROW
        update Machine_table
        SET Wear_tear_index = (new.Total_rep_count / 100 + DATEDIFF(CURDATE(),installment_date)) / 1000
        WHERE MachineID = NEW.MachineID;
"""
