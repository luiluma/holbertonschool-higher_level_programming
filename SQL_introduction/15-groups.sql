-- script that lists the number of records with the same score in the table
-- second_table of the database hbtn_0c_0,  result displays score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER by number DESC;