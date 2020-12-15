-- script that prepares a MySQL server for the project:
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev is: hbnb_dev_pwd
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev_db'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev_db'@'localhost';
