USE HotelDB;

CREATE VIEW customers_info
AS
SELECT A.NFC_ID, A.last_name, A.first_name, A.birth_date, A.id, A.id_type, A.id_issue, GROUP_CONCAT(distinct customer_phones.phone_number), GROUP_CONCAT(distinct customer_emails.email_address)
FROM customers A, customer_phones, customer_emails
WHERE A.NFC_ID = customer_emails.NFC_ID
    AND A.NFC_ID = customer_phones.NFC_ID
GROUP BY A.NFC_ID
ORDER BY A.NFC_ID DESC

