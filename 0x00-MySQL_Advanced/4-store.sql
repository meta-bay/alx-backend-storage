-- create a tringer that decreases quantity of an item base on order
DELIMITER //

CREATE TRIGGER dsr
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END//

DELIMITER ;
