CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    pin CHAR(4),
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    balance DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE DATABASE bank_system;

USE bank_system;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    pin CHAR(4) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- @block

INSERT INTO users (name, pin, is_admin) VALUES
('Alice Smith', '1234', FALSE),
('Bob Johnson', '2345', FALSE),
('Charlie Davis', '3456', FALSE),
('Diana Martinez', '4567', FALSE),
('Ethan Clark', '5678', FALSE),
('Fiona Lewis', '6789', FALSE),
('George Hall', '7890', FALSE),
('Hannah Allen', '8901', FALSE),
('Isaac Young', '9012', FALSE),
('Jenna King', '0123', FALSE),
('Kevin Scott', '1122', FALSE),
('Laura Green', '2233', FALSE),
('Michael Adams', '3344', FALSE),
('Natalie Baker', '4455', FALSE),
('Oliver Wright', '5566', FALSE),
('Penelope Hill', '6677', FALSE),
('Quentin Moore', '7788', FALSE),
('Rachel Turner', '8899', FALSE),
('Samuel Phillips', '9900', FALSE),
('Tina Campbell', '1010', FALSE);