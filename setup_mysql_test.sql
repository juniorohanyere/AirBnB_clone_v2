-- Preparation script to test MySQL server

-- Database hbnb_test_db creation if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Making the user hbnb_test
CREATE USER IF NOT EXISTS'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Privileges set for user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- hbnb_test_db database for test
-- Set new user (hbnb_test) privileges
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
