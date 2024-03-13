-- script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a user
CREATE USER IF NOT EXISTS 'user_od_2'@'localhost' IDENTIFIED BY 'user_od_2_pwd';
-- grants select privileges on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_od_2'@'localhost';