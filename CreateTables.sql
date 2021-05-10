IF OBJECT_ID('dbo.Phones', 'U') IS NOT NULL
 DROP TABLE dbo.Phones;
GO

IF OBJECT_ID('dbo.Emails', 'U') IS NOT NULL
 DROP TABLE dbo.Emails;
GO

IF OBJECT_ID('dbo.HasAccess', 'U') IS NOT NULL
 DROP TABLE dbo.HasAccess;
GO

IF OBJECT_ID('dbo.Visit', 'U') IS NOT NULL
 DROP TABLE dbo.Visit;
GO

IF OBJECT_ID('dbo.UseService', 'U') IS NOT NULL
 DROP TABLE dbo.UseService;
GO

IF OBJECT_ID('dbo.ProvideTo', 'U') IS NOT NULL
 DROP TABLE dbo.ProvideTo;
GO

IF OBJECT_ID('dbo.Register', 'U') IS NOT NULL
 DROP TABLE dbo.Register;
GO

IF OBJECT_ID('dbo.WithRegister', 'U') IS NOT NULL
 DROP TABLE dbo.WithRegister;
GO

IF OBJECT_ID('dbo.NoRegister', 'U') IS NOT NULL
 DROP TABLE dbo.NoRegister;
GO

IF OBJECT_ID('dbo.Customers', 'U') IS NOT NULL
 DROP TABLE dbo.Customers;
GO

IF OBJECT_ID('dbo.Areas', 'U') IS NOT NULL
 DROP TABLE dbo.Areas;
GO

IF OBJECT_ID('dbo.Services', 'U') IS NOT NULL
 DROP TABLE dbo.Services;
GO

-- Create the table Customers
CREATE TABLE dbo.Customers
(
 NFC_ID nvarchar(15) NOT NULL PRIMARY KEY, -- primary key column
 First_Name nvarchar(50) NOT NULL,
 Last_Name nvarchar(50) NOT NULL,
 Birth_Date date NOT NULL,
 Identification_Number nvarchar(20) NOT NULL,
 Identification_Type char(8) NOT NULL,
 Identification_Issue_Auth nvarchar(50) NOT NULL, 
 CHECK (Identification_Type in ('Passport', 'Identity'))
);
GO

-- Create the table Emails
CREATE TABLE dbo.Emails
(
 Email_Address nvarchar(80) NOT NULL PRIMARY KEY, -- primary key column
 NFC_ID nvarchar(15) NOT NULL FOREIGN KEY REFERENCES dbo.Customers(NFC_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE
);
GO

-- Create the table Phones
CREATE TABLE dbo.Phones
(
 Telephone nvarchar(20) NOT NULL PRIMARY KEY, -- primary key column
 NFC_ID nvarchar(15) NOT NULL FOREIGN KEY REFERENCES dbo.Customers(NFC_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE
);
GO

--Create the table Areas
CREATE TABLE dbo.Areas
(
 AREA_ID int NOT NULL PRIMARY KEY, --primary key column
 Area_Name nvarchar(40) NOT NULL,
 Number_of_Beds int,
 Area_Floor int NOT NULL,
 Area_Orientation nvarchar(2) NOT NULL,
 Area_Info nvarchar(100),
 CHECK (Area_Orientation in ('N', 'W', 'E', 'S', 'NE', 'NW', 'SE', 'SW')),
 CHECK (Area_Floor >= 0 AND Area_Floor < 6)
);
GO

-- Create the table Services
CREATE TABLE dbo.Services
(
 Service_ID int NOT NULL PRIMARY KEY, -- primary key column
 Service_Description nvarchar(100) NOT NULL,
 Service_Type nvarchar(13) NOT NULL,
 CHECK (Service_Type in ('With_Register', 'No_Register'))
);
GO

-- Create the table WithRegister
CREATE TABLE dbo.WithRegister
(
 Service_ID int NOT NULL,
 PRIMARY KEY (Service_ID),
 FOREIGN KEY (Service_ID) REFERENCES dbo.Services(Service_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 Service_Description nvarchar(100) NOT NULL,
 Service_Type nvarchar(13) NOT NULL,
 CHECK (Service_Type='With_Register')
);
GO

-- Create the table NoRegister
CREATE TABLE dbo.NoRegister
(
 Service_ID int NOT NULL,
 PRIMARY KEY (Service_ID),
 FOREIGN KEY (Service_ID) REFERENCES dbo.Services(Service_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 Service_Description nvarchar(100) NOT NULL,
 Service_Type nvarchar(13) NOT NULL,
 CHECK (Service_Type='No_Register')
);
GO

-- Create the table Register
CREATE TABLE dbo.Register
(
 NFC_ID nvarchar(15) NOT NULL,
 Service_ID int NOT NULL,
 PRIMARY KEY (NFC_ID, Service_ID),
 FOREIGN KEY (NFC_ID) REFERENCES dbo.Customers(NFC_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 FOREIGN KEY (Service_ID) REFERENCES dbo.WithRegister(Service_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 Registration_Time datetime NOT NULL 
);
GO

-- Create the table HasAccess
CREATE TABLE dbo.HasAccess
(
  NFC_ID nvarchar(15) NOT NULL,
  AREA_ID int NOT NULL,
  PRIMARY KEY (NFC_ID, AREA_ID), -- primary key column
  FOREIGN KEY (NFC_ID) REFERENCES dbo.Customers(NFC_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (AREA_ID) REFERENCES dbo.Areas(AREA_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  from_moment datetime NOT NULL,
  to_moment datetime NOT NULL
);
GO

-- Create the table Visit
CREATE TABLE dbo.Visit
(
  NFC_ID nvarchar(15) NOT NULL,
  AREA_ID int NOT NULL,
  PRIMARY KEY (NFC_ID, AREA_ID), -- primary key column
  FOREIGN KEY (NFC_ID) REFERENCES dbo.Customers(NFC_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (AREA_ID) REFERENCES dbo.Areas(AREA_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  enter datetime NOT NULL,
  leave datetime NOT NULL
);
GO

-- Create the table UseService
CREATE TABLE dbo.UseService
(
 DateAndTime datetime NOT NULL PRIMARY KEY, -- primary key column
 NFC_ID nvarchar(15) NOT NULL FOREIGN KEY REFERENCES dbo.Customers(NFC_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 Service_ID int NOT NULL FOREIGN KEY REFERENCES dbo.Services(Service_ID)
 ON DELETE CASCADE
 ON UPDATE CASCADE,
 Cost float,
 Describtion nvarchar(200) 
);
GO

-- Create the table ProvideTo
CREATE TABLE dbo.ProvideTo
(
  Service_ID int NOT NULL,
  AREA_ID int NOT NULL,
  PRIMARY KEY (Service_ID, AREA_ID), -- primary key column
  FOREIGN KEY (Service_ID) REFERENCES dbo.Services(Service_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (AREA_ID) REFERENCES dbo.Areas(AREA_ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);
GO
