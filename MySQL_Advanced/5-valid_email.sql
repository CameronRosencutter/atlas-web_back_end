-- Show users and update (or not) email
DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = FALSE; -- or 0, depending on how you're storing this attribute
    END IF;
END$$

DELIMITER ;