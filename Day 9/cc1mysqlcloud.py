import mysql.connector

conn=mysql.connector.connect(user='sanjoli04', password='sanjoli@1166', host='db4free.net', database='ssdatabase')

c=conn.cursor()

c.execute(""" CREATE TABLE students(
            Student_Name TEXT,
            Student_Age INTEGER,
            Student_Roll_no INTEGER,
            Student_Branch TEXT)
        """)

c.execute("INSERT INTO students VALUES ('Sanjoli',20,29,'CSE')")
c.execute("INSERT INTO students VALUES ('Ankit',18,49,'ECE')")
c.execute("INSERT INTO students VALUES ('Rocky',20,18,'CSE')")
c.execute("INSERT INTO students VALUES ('Saman',14,54,'IT')")
c.execute("INSERT INTO students VALUES ('Pragya',19,51,'ECE')")
c.execute("INSERT INTO students VALUES ('Nidhi',20,16,'ME')")
c.execute("INSERT INTO students VALUES ('Ram',17,11,'CSE')")
c.execute("INSERT INTO students VALUES ('Payal',10,45,'EE')")
c.execute("INSERT INTO students VALUES ('Anuu',18,27,'EE')")
c.execute("INSERT INTO students VALUES ('Sagar',18,03,'CV')")

c.execute("SELECT * FROM students")

print(c.fetchall())

