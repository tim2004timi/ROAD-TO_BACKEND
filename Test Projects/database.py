import sqlite3 as sq
from datetime import date


class DataBase:
    __PATH = r"my-data-base.db"

    def __init__(self):
        self._connection = sq.connect(self.__PATH)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self._cursor.close()
        if isinstance(exc_value, Exception):
            self._connection.rollback()
        else:
            self._connection.commit()
        self._connection.close()

    def execute(self, request: str):
        self._cursor.execute(request)

    def commit(self):
        self._connection.commit()

    def add_to_work(self, eng: int = 0, prg: int = 0, spt: int = 0):
        self._cursor.execute("INSERT INTO Work VALUES (?, ?, ?, ?)", (str(date.today()), eng, prg, spt))
        self.commit()

    def get_work(self):
        self._cursor.execute("SELECT * FROM Work")
        return self._cursor.fetchall()


def main():
    with DataBase() as db:
        db.add_to_work(1, 1, 1)
        print(db.get_work())


if __name__ == "__main__":
    main()
