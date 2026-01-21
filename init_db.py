import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    salary INTEGER,
    department TEXT,
    joining_date TEXT
)
""")


employees = [
    ("Suresh", "Naresh", "Patil", 45000, "Finance", "2018-06-10"),
    ("Suresh", "Ganesh", "Patil", 55000, "HR", "2020-02-15"),
    ("Suresh", "Naresh", "Patil", 60000, "IT", "2022-09-01"),
    ("Naresh", "Ashok", "Jadhav", 48000, "Sales", "2021-01-11"),
    ("Ganesh", "Prakash", "Patil", 52000, "QA", "2019-08-20"),
    
    # Additional 
    ("Ramesh", "Kumar", "Sharma", 47000, "Finance", "2019-03-12"),
    ("Ramesh", "Anil", "Sharma", 52000, "HR", "2020-07-21"),
    ("Vikram", "Suresh", "Joshi", 49000, "Sales", "2021-05-15"),
    ("Amit", "Rajesh", "Mehta", 53000, "QA", "2020-12-18"),

    ("Kiran", "Vikrant", "Deshmukh", 47000, "Finance", "2019-03-12"),
    ("Kiran", "Arjun", "Deshmukh", 52000, "HR", "2020-07-21"),
    ("Manish", "Rohan", "Patankar", 49000, "Sales", "2021-05-15"),
    ("Priya", "Sanjay", "Kulkarni", 53000, "QA", "2020-12-18"),

    ("Neha", "Tanmay", "Chaudhary", 47000, "Finance", "2019-03-12"),
    ("Neha", "Raghav", "Chaudhary", 52000, "HR", "2020-07-21"),
    ("Aditya", "Kartik", "Malhotra", 49000, "Sales", "2021-05-15"),
    ("Sneha", "Varun", "Saxena", 53000, "QA", "2020-12-18")
]


cursor.executemany("""
INSERT INTO employee
(first_name, middle_name, last_name, salary, department, joining_date)
VALUES (?, ?, ?, ?, ?, ?)
""", employees)

conn.commit()
conn.close()

print("Database created successfully")
