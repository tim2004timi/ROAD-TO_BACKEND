import sqlite3 as sq


cars = [
    ("Ferari", 20_000),
    ("Lamborghini", 23_000),
    ("Bugatti", 35_000)
]

with sq.connect("cars.db") as con:
    cur = con.cursor()

    # cur.executescript("""
    # INSERT INTO cars VALUES (NULL, 'Audi', 6500);
    # INSERT INTO cars VALUES (NULL, 'BMW', 7200);
    # INSERT INTO cars VALUES (NULL, 'Honda', 3000);
    # INSERT INTO cars VALUES (NULL, 'Mercedes', 7000);
    # """)

    cur.executemany("INSERT INTO cars VALUES (NULL, ?, ?)", cars)

    cur.execute("""
    SELECT * FROM cars
    """)

    print(cur.fetchall())
