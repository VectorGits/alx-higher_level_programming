-- Script that creates the MySQL server user user_0d_1.
-- set passeord to "user_od_1_pwd" and Grant all privileges on all databases of the MySQL server to user_0d_1.

CREATE USER IF NOT EXISTS 'user_od_1'@'localhost'
IDENTIFIED BY 'user_od_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_od_1'@'localhost' WITH GRANT OPTION;
