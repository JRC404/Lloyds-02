# SQL

* Structured Query Language
* Probably the closest thing to spoken / written English you're going to get in Development

## Different SQL flavours

* MySQL (C#, JavaScript, Java, Swift, C++)
* MS-SQL (C#, JavaScript)
* PostgreSQL (Java)
* AzureSQL (Azure, MS)
* SQLite (Web-based and free... and painful.)
* RDS (Amazon)
* OracleSQL (Java)
* SQL Server (MS)
* Many more...

## SQL Methods / Queries

* CRUD: 
    * INSERT INTO / CREATE (CREATE)
    * SELECT (READ)
    * UPDATE (UPDATE)
    * DELETE (DELETE)

## The process

* Create a Database (Schema) (DONE)
* Create a table inside of the database (DONE)
* Insert information into the table (DONE)
* Update the information (DONE)
* Alter the table (DONE)
* Delete things for fun
* Delete things for evil purposes
* Drop tables...

* Talk about the danger zone

## Danger Zone

### Update

```sql
-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

-- Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'WHERE EmployeeID = 3' at line 1

-- Error Code: 1046. No database selected Select the default DB to be used by double-clicking its name in the SCHEMAS list in the sidebar.


```

## Installing SQL

* Install the server of choice
    * Create credentials
    * Default user: **root**
    * Password: MyPassword1234
* Select your IDE (Development Environment)
    * MySQL Workbench
    * Azure Data Studio
    * VSCode
* Login to the server using the credentials and server address

## The role of a Quality Engineer in Data

* Ensure the database is able to be connected to
* Ensure the database rejects incorrect information
* Ensure the SQL queries return data in the correct format
* Verification and validation are present
* User permissions are in place
* CRUD is present:
    * Can the application perform all 4 actions?
    * Do the user permissions stop certain groups performing all 4 actions?

