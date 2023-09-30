class PrintError(Exception):
    """Исключение при работе с принтером"""

    def __init__(self, *args):
        self.message = args[0] if args else ""

    def __str__(self):
        return f"Ошибка: {self.message}"


class Printer:
    def __init__(self, text):
        self.text = text

    def print(self):
        if self.is_working():
            print(self.text)
        else:
            raise PrintError("принтер не отвечает")

    @staticmethod
    def is_working():
        return False


printer = Printer("Hello")
printer.print()
