-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)

BEGIN
    DECLARE _id INT;

    SELECT id INTO _id FROM projects WHERE name = project_name;
    IF _id IS NULL THEN
        INSERT INTO projects (name) VALUE (project_name);
        SET _id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, _id, score);

END; //

DELIMITER ;