-- Database ensure
CREATE DATABASE IF NOT EXISTS python;

-- Use database
USE python;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(100)
);

-- Optional: ek dummy record
INSERT INTO students (id, name, course) 
VALUES (1, 'Santosh Kumar', 'DevOps')
ON DUPLICATE KEY UPDATE name=VALUES(name), course=VALUES(course);
