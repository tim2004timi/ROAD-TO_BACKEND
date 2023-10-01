class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = "заголовок"
    content = "контент"
    photo = "путь к фото"


w = Women()
print(w.title, w.content, w.__dict__)
