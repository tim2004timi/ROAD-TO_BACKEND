import sqlite3 as sq


with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT id, name, score FROM users
    WHERE score > 500 AND old > 17 AND sex IN (1)
    ORDER BY score DESC
    LIMIT 4
    OFFSET 0
    """)

    result = cur.fetchall()
    print(result)
