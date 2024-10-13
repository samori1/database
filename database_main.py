import sqlite3

db = None

try:
    # Create database
    db = sqlite3.connect('python_programming.db')
    # Create a cursor object
    cursor = db.cursor()
    # Create a table
    cursor.execute('''
                CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                                            grade INTEGER)
    ''')
    # Create a list of data ready to insert into table
    students_grades = [(55,'Carl Davis', 61),(66,'Dennis Fredrickson',88),(77,'Jane Richards',78),
                    (12,'Peyton Sawyer', 45),(2,'Lucas Brooke',99)]
    # Insert data into table
    cursor.executemany('''INSERT INTO python_programming(id, name, grade) 
                VALUES(?,?,?)''', students_grades)
    # Select all records with a grade between 60 and 80
    cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
    # Change Carl Davis' grade to 65
    cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
    # Delete Dennis Fredrickson's data
    cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
    # Change the grade of all students with an id greater than 55 to 80
    cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")
    
    db.commit()
    
    cursor.execute("SELECT * FROM python_programming")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
except Exception as e:
    print("An error has occured:", e)
    if db is not None:
        db.rollback()
        print("Transaction rolled back.")
    raise e
finally:
    if db is not None:
        db.close()
        print("Database connection closed.")
    else:
        print("Database connection was not established.")