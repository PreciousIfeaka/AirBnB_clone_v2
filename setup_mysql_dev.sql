-- This script prepares a MySql server for this project.
-- Creates a database 'hbnb_dev_db'
-- Creates a new user 'hbnb_dev' in localhost
-- Sets the password of hbnb_dev to 'hbnb_dev_pwd'.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
