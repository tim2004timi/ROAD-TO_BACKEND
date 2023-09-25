class DataBase:
    __instance = None
    __atr = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
        DataBase.__atr = False
        print(self.user, "__del__")

    def __init__(self, user, psw):
        if not DataBase.__atr:
            self.user = user
            self.psw = psw
            DataBase.__atr = True

    def method(self):
        pass


data_base = DataBase("root", 123)
data_base2 = DataBase("tim", 345)
print(data_base, data_base2.user)
