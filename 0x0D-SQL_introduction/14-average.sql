-- script that computes the score average of all records in the table second_table
SELECT SUM(score) / 5 as average
FROM second_table;
