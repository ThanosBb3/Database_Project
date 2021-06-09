USE HotelDB;

CREATE VIEW services_sales
AS
SELECT A.SERVICE_ID, A.category, A.service_description, ROUND(SUM(B.cost),2)
FROM services A, useService B
WHERE A.SERVICE_ID = B.SERVICE_ID
    AND A.SERVICE_ID <> 1 
GROUP BY A.SERVICE_ID
ORDER BY A.SERVICE_ID ASC