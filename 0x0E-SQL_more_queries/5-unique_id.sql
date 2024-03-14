--  script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id
	(id DEFAULT 1, 
	UNIQUE(ID), 
	name VARCHAR(256));
