"""Layout.
- Instead update wear and tear score.
"""

wear_and_tear_trigger = """
DELIMITER //

CREATE TRIGGER update_wear_and_tear
AFTER UPDATE
ON Machine_stats_table
FOR EACH ROW
"""

## FINISH THIS BY UPDATING THE WEAR AND TEAR INDEX BASED ON REPS AND INSTALLMENT DATE