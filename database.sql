CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(255) NOT NULL,
    rank INT,
    wins INT,
    losses INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE commands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    command_name VARCHAR(255) NOT NULL,
    player_name VARCHAR(255),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
