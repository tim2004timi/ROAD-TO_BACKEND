class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + str(psw))

    class Meta:
        ordering = ["id"]

        def __init__(self, access):
            self._access = access


w = Women("root", 123456)
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)
