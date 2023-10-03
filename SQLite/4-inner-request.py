import sqlite3 as sq


with sq.connect("students.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT name, subject, mark FROM marks A
    JOIN students B ON A.id = B.id
    WHERE mark <= (SELECT mark FROM marks
    WHERE id = 0 AND subject LIKE 'Math') 
    AND subject LIKE 'Math'
    """)

    for row in cur.fetchall():
        print(row)
