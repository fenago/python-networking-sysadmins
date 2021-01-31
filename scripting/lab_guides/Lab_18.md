<img align="right" src="./logo.png">

Lab 18. MySQL and SQLite Database Administrations
--------------------------------------------------------------



In this lab, you will learn about MySQL and SQLite database
administration. You will learn to install MySQL and SQLite. You will
also learn how to create users, grant privileges, create databases,
create tables, insert data into a table, and view all records from the
table specific records, and update and delete the data.

In this lab, you will learn the following:


-   MySQL database administration
-   SQLite database administration



MySQL database administration
------------------------------------------------



This section will cover MySQL database
administration using Python. You already know Python has
various modules for `mysql`
database administration. So, we will learn about the MySQLdb module
here. The `mysqldb` module is an interface for MySQL database
server and is used to provide Python database API.

Let\'s learn how to install MySQL and a
Python `mysqldb` package. For this, run the following command
in your Terminal:


```
$ sudo apt install mysql-server
```

This command installs the MySQL server and various other packages. While
installing the package, we are prompted to enter a password for the
MySQL root account:


-   The following code is used for checking for the `mysqldb`
    package to install:

```
$ apt-cache search MySQLdb
```


-   And the following is for installing the Python interface for MySQL:

```
$ sudo apt-get install python3-mysqldb
```


-   Now, we will check if `mysql` is installed properly or
    not. For this, run the following command in Terminal:

```
student@ubuntu:~$ sudo mysql -u root -p
```

Once the command runs, you will get the following output:


```
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.24-0ubuntu0.18.04.1 (Ubuntu)



Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

By running `sudo mysql -u root -p`, you will get
the `mysql` console. There are some commands used for listing
databases and tables, and using the database to store our work. We will
see them one by one:


-   This is for listing all the databases:

```
show databases;
```


-   And this is for using the database:

```
use database_name;
```

Whenever we come out of the MySQL console and log in again after some
time, we must use the `use database_name;` statement. The
purpose of using this command is that our work will be saved in our
database. We can understand this in detail with the following examples:


-   The following code is used for listing all the tables:

```
show tables;
```

These are the commands we use for listing databases, using the database,
and listing the tables.

Now, we will create a database using a create database statement in
the `mysql` console. Now, open the `mysql` console
using `mysql -u root -p`, then enter your password, which you
entered while installing, and press [*Enter*]. Next, create
your database. In this section, we are going to create a database named
`test` and we will use this database throughout this section:


```
student@ubuntu:~/work/mysql_testing$ sudo mysql -u root -p

Output:
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.7.24-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.


Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


mysql>
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.10 sec)

mysql> create database test;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
5 rows in set (0.00 sec)

mysql> use test;
Database changed
mysql>
```

First, we listed all the databases using show databases. Next, we
created our database test using the create
`database` statement. Again, we executed show databases to
find whether our database is created or not. Our database is now
created. Next, we used that database to store the work we are doing.

Now, we are going to create a user and grant the privileges to that
user. Run the following commands:


```
mysql> create user 'test_user'@'localhost' identified by 'test123';
Query OK, 0 rows affected (0.06 sec)

mysql> grant all on test.* to 'test_user'@'localhost';
Query OK, 0 rows affected (0.02 sec)

mysql>
```

We created a `test_user` user; the password for that user is
`test123`. Next, we grant all the privileges to
our `test_user` user. Now, come out of the `mysql`
console by running a `quit;` or `exit;` command.

Now, we are going to see some examples for getting a database version,
creating a table, inserting some data into the table, updating the data,
and deleting the data.



### Getting a database version



First, we will see an example of getting the database version. For that, we will create
a `get_database_version.py`script and write the following
content in it:


```
import MySQLdb as mdb
import sys

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute("SELECT VERSION()")
version = cur_obj.fetchone()
print ("Database version: %s " % version)

con_obj.close()
```


### Note

It is very important to follow the previous steps before running this
script; they should not be skipped. 


Run the script and you will get the following output:


```
student@ubuntu:~/work/mysql_testing$ python3 get_database_version.py
Output:
Database version: 5.7.24-0ubuntu0.18.04.1
```

In the preceding example, we got the database version. For that, first
we imported the MySQLdb module. Then we wrote the connection string. In
the connection string, we mentioned our username, password, and database
name. Next, we created a cursor object that is used for executing a SQL
query. In `execute()`, we passed an SQL
query. `fetchone()` retrieves the next row of query result.
Next, we printed the result. The `close()` method closes the
database connection.


### Creating a table and inserting data



Now, we are going to create a table and we
will insert some data into it. For that,
create a `create_insert_data.py`script and write the following
content in it:


```
import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')
with con_obj:
            cur_obj = con_obj.cursor()
            cur_obj.execute("DROP TABLE IF EXISTS courses")
            cur_obj.execute("CREATE TABLE courses(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(100))")
            cur_obj.execute("INSERT INTO courses(Name) VALUES('Harry Potter')")
            cur_obj.execute("INSERT INTO courses(Name) VALUES('Lord of the rings')")
            cur_obj.execute("INSERT INTO courses(Name) VALUES('Murder on the Orient Express')")
            cur_obj.execute("INSERT INTO courses(Name) VALUES('The adventures of Sherlock Holmes')")
            cur_obj.execute("INSERT INTO courses(Name) VALUES('Death on the Nile')")

print("Table Created !!")
print("Data inserted Successfully !!")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work/mysql_testing$ python3 create_insert_data.py

Output:
Table Created !!
Data inserted Successfully !!
```

To check whether your table is created successfully or not, open your
`mysql` console and run the following commands:


```
student@ubuntu:~/work/mysql_testing$ sudo mysql -u root -p

Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.7.24-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


mysql>
mysql>
mysql> use test;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A


Database changed
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| courses          |
+----------------+
1 row in set (0.00 sec)
```

You can see that your table courses is created.


### Retrieving the data



To retrieve the data from the table, we use the `select`
statement. Now, we are going to retrieve the data from our courses table. For that, create
a `retrieve_data.py`script and write the following content in
it:


```
import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')
with con_obj:
            cur_obj = con_obj.cursor()
            cur_obj.execute("SELECT * FROM courses")
            records = cur_obj.fetchall()
            for r in records:
                        print(r)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work/mysql_testing$ python3 retrieve_data.py

Output:
(1, 'Harry Potter')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
(5, 'Death on the Nile')
```

In the preceding example, we retrieved data from tables. We used the
MySQLdb module. We wrote a connection string and created a cursor object
to execute the SQL query. In `execute()`, we wrote an SQL
`select` statement. And last, we printed the records.


### Updating the data



Now, if we want to make some changes in the
records, we can use an SQL `update` statement. We are going to
see an example of an `update` statement. For that, create
a `update_data.py`script and write following content in it:


```
import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute("UPDATE courses SET Name = 'Fantastic Beasts' WHERE Id = 1")
try:
    con_obj.commit()
except:
    con_obj.rollback()
```

Run the script as follows:


```
student@ubuntu:~/work/mysql_testing$ python3 update_data.py
```

Now, to check if your record is updated or not, run
`retrieve_data.py` as follows:


```
student@ubuntu:~/work/mysql_testing$ python3 retrieve_data.py

Output:
(1, 'Fantastic Beasts')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
(5, 'Death on the Nile')
```

You can see your data for ID `1` is updated. In the preceding
example, in `execute()`, we have written an `update`
statement that will update the data for ID `1`.


### Deleting the data



To delete a particular record from your
table, use a `delete` statement. We are going to see an
example of deleting data. Create a `delete_data.py`script and
write the following content in it:


```
import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute("DELETE FROM courses WHERE Id = 5");
try:
            con_obj.commit()
except:
            con_obj.rollback()
```

Run the script as follows:


```
student@ubuntu:~/work/mysql_testing$ python3 delete_data.py
```

Now, to check whether your record is deleted or not, run
the `retrieve_data.py` script as follows:


```
student@ubuntu:~/work/mysql_testing$ python3 retrieve_data.py

Output:
(1, 'Fantastic Beasts')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
```

You can see your record, whose ID is `5`, is deleted. In the
preceding example, we used the `delete` statement to delete a
particular record. Here, we deleted the record whose ID is
`5`. You can also delete the record according to any field
name of your choice.



SQLite database administration
-------------------------------------------------



In this section, we are going to learn how to install and use SQLite.
Python has the `sqlite3` module to do SQLite database tasks.
SQLite is a serverless, zero configuration, transactional SQL database
engine. SQLite is very fast and lightweight. The entire database is
stored in a single disk file.

Now, we will install SQLite first. Run the
following command in your Terminal:


```
$ sudo apt install sqlite3
```

In this section, we are going to learn following the operations:
creating database, creating tables, inserting data into table,
retrieving the data, and updating and deleting the data from table. We
will see each operation one by one.

Now, first, we will see how to create a database in SQLite. To create a
database, you simply have to write the command in your Terminal as
follows:


```
$ sqlite3 test.db
```

After running this command, you will get the `sqlite` console
opened in your Terminal as follows:


```
student@ubuntu:~$ sqlite3 test.db
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite>
```

There you go, your database has been created by simply running
`sqlite3 test.db`.



### Connecting to the database



Now, we will see how to connect to the
database. For that, we are going to create a script. Python already has
a `sqlite3` module included in the standard library. We just
have to import it whenever we are going to work with SQLite. Create a
`connect_database.py`script and write the following content in
it:


```
import sqlite3

con_obj = sqlite3.connect('test.db')
print ("Database connected successfully !!")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work $ python3 connect_database.py

Output:
Database connected successfully !!
```

In the preceding example, we imported the `sqlite3` module to
perform the functionality. Now, check your directory and you will find
the `test.db` file created in your directory.


### Creating a table



Now, we are going to create a table in our
database. For that, we will create
a `create_table.py`script and write the following content in
it:


```
import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
            cur_obj = con_obj.cursor()
            cur_obj.execute("""CREATE TABLE courses(title text, author text)""")

print ("Table created")
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work $ python3 create_table.py

Output:
Table created
```

In the preceding example, we created a table courses using
a `CREATE TABLE` statement. First, we established a connection
with our database using `test.db`. Next, we created a cursor
object that we used to execute the SQL query on our database.


### Inserting the data



Now, we will insert the data into our table. For that, we will
create a `insert_data.py`script and
write the following content in it:


```
import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
            cur_obj = con_obj.cursor()
            cur_obj.execute("INSERT INTO courses VALUES ('Pride and Prejudice', 'Jane Austen')")
            cur_obj.execute("INSERT INTO courses VALUES ('Harry Potter', 'J.K Rowling')")
            cur_obj.execute("INSERT INTO courses VALUES ('The Lord of the Rings', 'J. R. R. Tolkien')")
            cur_obj.execute("INSERT INTO courses VALUES ('Murder on the Orient Express', 'Agatha Christie')")
            cur_obj.execute("INSERT INTO courses VALUES ('A Study in Scarlet', 'Arthur Conan Doyle')")
            con_obj.commit()

print("Data inserted Successfully !!")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 insert_data.py

Output:
Data inserted Successfully !!
```

In the preceding example, we inserted some data into our table. For
that, we used `insert` in the SQL statement. By using
`commit()`, we are telling the database to save all the
current transactions.


### Retrieving the data



Now, we are going to retrieve the data from
the table. For that, create a `retrieve_data.py`script and
write the following content in it:


```
import sqlite3

con_obj = sqlite3.connect('test.db')
cur_obj = con_obj.execute("SELECT title, author from courses")
for row in cur_obj:
            print ("Title = ", row[0])
            print ("Author = ", row[1], "\n")

con_obj.close()
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work$ python3 retrieve_data.py

Output:
Title =  Pride and Prejudice
Author =  Jane Austen

Title =  Harry Potter
Author =  J.K Rowling

Title =  The Lord of the Rings
Author =  J. R. R. Tolkien

Title =  Murder on the Orient Express
Author =  Agatha Christie

Title =  A Study in Scarlet
Author =  Arthur Conan Doyle
```

In the preceding example, we imported the `sqlite3` module.
Next, we connected with our `test.db` database . To retrieve
the data, we used the `select` statement. And, last, we
printed the retrieved data.

You can also retrieve the data in the `sqlite3` console. For
that, start the SQLite console first and then retrieve the data as
follows:


```
student@ubuntu:~/work/sqlite3_testing$ sqlite3 test.db

Output:
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite>
sqlite> select * from courses;
Pride and Prejudice|Jane Austen
Harry Potter|J.K Rowling
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
sqlite>
```


### Updating the data



We can update the data from our table using
the `update` statement. Now, we are going to see an example of
updating data. For that, create a `update_data.py`script and
write the following content in it:


```
import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
cur_obj = con_obj.cursor()
            sql = """
                        UPDATE courses
                        SET author = 'John Smith'
                        WHERE author = 'J.K Rowling'
                        """
            cur_obj.execute(sql)

print("Data updated Successfully !!")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work $ python3 update_data.py

Output:
Data updated Successfully !!
```

Now, to check that the data is actually updated or not, you can run
`retrieve_data.py`, or else you can go to the SQLite console
and run `select * from courses;`. You will get the updated
output as follows:


```
By running retrieve_data.py:

Output:
student@ubuntu:~/work$ python3 retrieve_data.py
Title =  Pride and Prejudice
Author =  Jane Austen

Title =  Harry Potter
Author =  John Smith

Title =  The Lord of the Rings
Author =  J. R. R. Tolkien

Title =  Murder on the Orient Express
Author =  Agatha Christie

Title =  A Study in Scarlet
Author =  Arthur Conan Doyle

Checking on SQLite console:

Output:
student@ubuntu:~/work$ sqlite3 test.db
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite>
sqlite> select * from courses;
Pride and Prejudice|Jane Austen
Harry Potter|John Smith
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
sqlite>
```


### Deleting the data



Now, we will see an example of deleting data from a table. We are going to do this using the
`delete` statement. Create
a `delete_data.py`script and write the following content in
it:


```
import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
            cur_obj = con_obj.cursor()
sql = """
                        DELETE FROM courses
                        WHERE author = 'John Smith'
                        """
            cur_obj.execute(sql)

print("Data deleted successfully !!")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work $ python3 delete_data.py

Output:
Data deleted successfully !!
```

In the preceding example, we deleted a record from a table. We used
the `delete` SQL statement. Now, to check whether the data is
deleted successfully or not, run `retrieve_data.py` or start
the SQLite console, as follows:


```
By running retrieve_data.py

Output:
student@ubuntu:~/work$ python3 retrieve_data.py
Title =  Pride and Prejudice
Author =  Jane Austen

Title =  The Lord of the Rings
Author =  J. R. R. Tolkien

Title =  Murder on the Orient Express
Author =  Agatha Christie

Title =  A Study in Scarlet
Author =  Arthur Conan Doyle
```

You can see the record whose author was `john smith` is
deleted:


```
Checking on SQLite console:

Output:
student@ubuntu:~/work$ sqlite3 test.db
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite>
sqlite> select * from courses;
Pride and Prejudice|Jane Austen
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
sqlite>
```



Summary
--------------------------



In this lab, we learned about MySQL as well as SQLite database
administration. We created databases and tables. We then inserted a few
records in tables. Using the `select` statement, we retrieved
the records. We also learned about updating and deleting the data.



Questions
----------------------------




1.  What is database used for?
2.  What is CRUD in a database?
3.  Can we connect a remote database? If yes, explain with an example.
4.  Can we write triggers and procedures inside Python code?
5.  What are DML and DDL statements?
