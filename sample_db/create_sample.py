import sqlite3

connection=sqlite3.connect('sample.db')
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary REAL,
    join_date TEXT
)''')
cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    budget REAL,
    status TEXT
);
'''
)
cursor.execute('''
    INSERT INTO employees (name, department, salary, join_date) VALUES
('Arjun Sharma', 'Engineering', 85000, '2021-03-15'),
('Priya Patel', 'Marketing', 62000, '2020-07-01'),
('Rohit Verma', 'Engineering', 92000, '2019-11-20'),
('Sneha Iyer', 'HR', 55000, '2022-01-10'),
('Karan Mehta', 'Engineering', 78000, '2021-08-25'),
('Anjali Singh', 'Marketing', 67000, '2020-03-30'),
('Vikram Nair', 'Finance', 88000, '2018-06-15'),
('Pooja Gupta', 'HR', 52000, '2023-02-01'),
('Rahul Joshi', 'Finance', 95000, '2017-09-10'),
('Neha Kapoor', 'Engineering', 81000, '2022-05-20')
''')

cursor.execute('''
    INSERT INTO projects (name, department, budget, status) VALUES
('Website Redesign', 'Marketing', 150000, 'completed'),
('AI Chatbot', 'Engineering', 300000, 'active'),
('HR Portal', 'HR', 80000, 'active'),
('Financial Dashboard', 'Finance', 200000, 'completed'),
('Mobile App', 'Engineering', 250000, 'active'),
('Brand Campaign', 'Marketing', 120000, 'planning'),
('Payroll System', 'Finance', 175000, 'completed'),
('Employee Training', 'HR', 45000, 'planning'),
('Data Pipeline', 'Engineering', 320000, 'active'),
('Annual Report', 'Finance', 30000, 'completed')
''')


connection.commit()
connection.close()