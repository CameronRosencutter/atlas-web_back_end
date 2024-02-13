-- Create the trigger
DELIMITER //

CREATE TRIGGER after_order_decrease
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END//

DELIMITER ;