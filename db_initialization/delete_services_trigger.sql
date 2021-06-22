use HotelDB;
DELIMITER //
DROP TRIGGER IF EXISTS delete_services
//
CREATE TRIGGER delete_services AFTER DELETE
ON services
FOR EACH ROW
BEGIN
   IF (not OLD.register_required) THEN
   DELETE FROM services_No_Register
      WHERE (SERVICE_ID=OLD.SERVICE_ID);
    
    ELSE  
   DELETE FROM services_With_Register
      WHERE (SERVICE_ID=OLD.SERVICE_ID);
END IF;
END;//
DELIMITER ;