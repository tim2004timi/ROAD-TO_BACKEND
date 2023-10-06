import sqlite3 as sq


def read_picture(file_name):
    try:
        with open(file_name, "rb") as file:
            return file.read()
    except IOError as e:
        print(e)


def write_picture(img):
    try:
        with open("out.jpeg", "wb") as file:
            file.write(img)
    except IOError as e:
        print(e)


with sq.connect("cars.db") as con:
    # Преобразуем в Row
    con.row_factory = sq.Row
    cur = con.cursor()

    # Можем обращаться по ключу
    cur.execute("SELECT * FROM cars")
    for result in cur:
        print(result["name"], result["price"])

    cur.execute("""
    CREATE TABLE IF NOT EXISTS pictures (
    name TEXT,
    picture BLOB);
    """)

    # Запись бинарника в базу
    image = read_picture("bmw.jpeg")
    if image:
        image = sq.Binary(image)
        cur.execute("INSERT INTO pictures VALUES ('BMW', ?)", (image, ))

    # Чтение бинарника из базы
    cur.execute("SELECT picture FROM pictures")
    image = cur.fetchone()['picture']
    write_picture(image)

    # Получение SQL для воссоздания базы
    for sql in con.iterdump():
        print(sql)
