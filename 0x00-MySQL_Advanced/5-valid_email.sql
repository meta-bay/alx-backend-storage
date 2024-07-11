-- validate email upon change
DELIMITER //

CREATE TRIGGER vld_e
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END//

DELIMITER ;
