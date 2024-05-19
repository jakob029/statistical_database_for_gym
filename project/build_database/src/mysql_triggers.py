"""Layout.
- Instead update wear and tear score.
"""

mysql_triggers = """
CREATE TRIGGER update_wear_and_tear_insert AFTER INSERT ON Machine_stats_table
FOR EACH ROW
        update Machine_table
        SET Wear_tear_index = ((select machine_total_reps(NEW.MachineID)) / 50 + DATEDIFF(CURDATE(),installment_date)) / 1000
        WHERE MachineID = NEW.MachineID;

CREATE TRIGGER update_wear_and_tear_update AFTER UPDATE ON Machine_stats_table
FOR EACH ROW
        update Machine_table
        SET Wear_tear_index = ((select machine_total_reps(NEW.MachineID)) / 50 + DATEDIFF(CURDATE(),installment_date)) / 1000
        WHERE MachineID = NEW.MachineID;
"""
