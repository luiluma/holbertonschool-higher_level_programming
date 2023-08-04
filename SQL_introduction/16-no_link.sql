-- script that lists all records of the table second_table of the database
--  hbtn_0c_0, results display the score and the name in desc way
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;