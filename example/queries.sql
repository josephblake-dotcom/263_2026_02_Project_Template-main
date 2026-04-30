-- queries to run to create the database for the example to run

-- Create the demo_players table
CREATE TABLE demo_players (
    ID varchar(20) PRIMARY KEY,
    Name varchar(100),
    Color varchar(50),
    Wins int,
    Losses int,
    Gold int
);

-- Stored procedure to update a player's score (Wins)
DELIMITER //
CREATE PROCEDURE UpdatePlayerScore(IN player_id varchar(20), IN new_wins int)
BEGIN
    UPDATE demo_players 
    SET Wins = new_wins 
    WHERE ID = player_id;
END //
DELIMITER ;

-- Stored procedure to query player statistics
DELIMITER //
CREATE PROCEDURE GetPlayerStats()
BEGIN
    SELECT
        COUNT(*) as TotalPlayers,
        SUM(Wins) as TotalWins,
        SUM(Losses) as TotalLosses,
        AVG(Gold) as AverageGold,
        MAX(Wins) as MaxWins
    FROM demo_players;
END //
DELIMITER ;

-- Create log table for nightly batch process
CREATE TABLE IF NOT EXISTS demo_scorelog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    LogDate DATE,
    PlayerID varchar(20),
    PlayerName varchar(100),
    Wins INT,
    Losses INT,
    Gold INT
);

-- Stored procedure for nightly batch process - log end of day scores
DELIMITER //
CREATE PROCEDURE LogEndOfDayScores()
BEGIN
    INSERT INTO demo_scorelog (LogDate, PlayerID, PlayerName, Wins, Losses, Gold)
    SELECT CURDATE(), ID, Name, Wins, Losses, Gold
    FROM demo_players
    WHERE Wins > 20;
END //
DELIMITER ;

-- Insert sample data
INSERT INTO demo_players (ID, Name, Color, Wins, Losses, Gold) VALUES
('P001', 'James Anderson', 'Red', 15, 8, 450),
('P002', 'Emily Roberts', 'Blue', 12, 10, 380),
('P003', 'Michael Thompson', 'Green', 20, 5, 600),
('P004', 'Sarah Wilson', 'Yellow', 8, 15, 250),
('P005', 'David Martinez', 'Purple', 25, 3, 750),
('P006', 'Jessica Taylor', 'Orange', 18, 7, 520),
('P007', 'Christopher Davis', 'Black', 10, 12, 310),
('P008', 'Amanda White', 'Pink', 22, 4, 680),
('P009', 'Daniel Harris', 'Red', 14, 9, 420),
('P010', 'Jennifer Clark', 'Blue', 16, 6, 490),
('P011', 'Matthew Lewis', 'Green', 9, 14, 280),
('P012', 'Ashley Walker', 'Yellow', 28, 2, 850),
('P013', 'Andrew Hall', 'Purple', 11, 11, 340),
('P014', 'Stephanie Young', 'Orange', 19, 8, 560),
('P015', 'Joshua King', 'Black', 23, 5, 710),
('P016', 'Michelle Wright', 'Pink', 7, 16, 220),
('P017', 'Ryan Scott', 'Red', 17, 7, 500),
('P018', 'Kimberly Torres', 'Blue', 13, 10, 390),
('P019', 'Brandon Nguyen', 'Green', 21, 4, 640),
('P020', 'Laura Hill', 'Yellow', 6, 17, 190),
('P021', 'Justin Flores', 'Purple', 24, 6, 730),
('P022', 'Samantha Green', 'Orange', 5, 18, 160),
('P023', 'Kevin Adams', 'Black', 26, 3, 800),
('P024', 'Rachel Nelson', 'Pink', 12, 9, 370),
('P025', 'Brian Carter', 'Green', 30, 1, 900);
