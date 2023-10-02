import sqlite3 as sq


with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT users.name, SUM(games.score) AS sum
    FROM games
    LEFT JOIN users ON games.id = users.id
    GROUP BY users.name
    ORDER BY sum
    """)

    for row in cur.fetchall():
        print(row)
