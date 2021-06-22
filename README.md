# Database_Project

## Overview
This is a Project for Databases class at NTUA.

The project is an information system about a hotel. 

The database of the app is populated initially by data carefully selected to make sense. 

* In the app the hotel receptionist can add, update or delete a customer, register a specific customer to a room or other services that require registration.


* A hotel manager can also see other useful information about the hotel such as:

    - Visit Records for every service provided by the hotel based on date and cost filters

    - Customer Info and Services Sales

    - Statistics about the busiest/most popular areas and services based on age group and time period filters

    - Special Tab for COVID-19 emergency that informs about the infected customer's area visits and potential high-risk contacts


## Requirements
* mysql 8.0.25

* flask 1.1.2

* mysql_connector 2.2.9

* numpy 1.20.1

* pandas 1.2.3

## ER Diagram
![image](https://user-images.githubusercontent.com/71256846/122912231-c62b9c00-d360-11eb-8d39-bcc8eba0fa2b.png)

## Relational Diagram
![image](https://user-images.githubusercontent.com/71256846/122906264-a72a0b80-d35a-11eb-800a-316c1636cbdb.png)

## Installation
Step 1: At first, initialize a mysql database at a localhost.
<br />
<br />
<br />
Step 2: Then, run the folowing command in terminal, using your credentials in order to connect in mysql host:
```bash
mysql --user=“your user name” --password=”your password” --host=localhost
```
<br />
<br />
Step 3: Run the following inside mysql command prompt, strictly at this order:


```bash
Source “path of the HotelDB.sql file” 
```


```bash
Source “path of the indexes.sql file”
```

```bash
Source “path of the customers_view.sql file”
```

```bash
Source “path of the services_view.sql file”
```
<br />
Step 4: Back at the Terminal run:
```bash
git clone https://github.com/ThanosBb3/Database_Project
```
<br />
<br />
<br />
Step 5: Add your Database credentials in the following files:

*	"app\backend\home.py"

*	"app\backend\register.py"

*	"app\__init__.py"

*	"db_initialization\connection.py"
<br />
<br />
Step 6: Run 

```bash
python main_db.py
```

to add the data on your Database.
<br />
<br />
<br />
Step 7: Now that everything is set up run:

```bash
python main_app.py
```

and open your browser on http://localhost:8765/ to see the app.

