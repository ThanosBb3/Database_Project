use HotelDB;
DELIMITER //
DROP TRIGGER IF EXISTS insert_services
//
CREATE TRIGGER insert_services AFTER INSERT
ON services
FOR EACH ROW
BEGIN
   IF (not NEW.register_required) THEN
   INSERT INTO services_No_Register
      (SERVICE_ID)
   VALUES
      (NEW.SERVICE_ID);
    
    ELSE  
   INSERT INTO services_With_Register
      (SERVICE_ID)
   VALUES
      (NEW.SERVICE_ID);
END IF;
END;//
DELIMITER ;