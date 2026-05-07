USE josephblake;

DROP PROCEDURE IF EXISTS UpdateGameStatus;
DELIMITER $$

CREATE PROCEDURE UpdateGameStatus (
    IN p_GameNo INT,
    IN p_NewWinPoints INT,
    OUT numberChanged INT
)
BEGIN
    UPDATE Game
    SET Win_Points = p_NewWinPoints
    WHERE Game_No = p_GameNo;

    SET numberChanged = ROW_COUNT();
END$$

DELIMITER ;

Select * From Game;
CALL UpdateGameStatus(1, 120, @numberChange);
SELECT @numberChange;
SELECT * FROM Game;
