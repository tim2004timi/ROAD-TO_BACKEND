from jinja2 import Template
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    old: int


tim = Person("Tim", 19)

tp = Template("I'm {{ p.name }} and {{ p.old }} years old")
message = tp.render(p=tim)

print(message)

# ------------------------------------------------------------

dct = {"name": "Tim", "age": 19}

text = tp.render(p=dct)

print(text)
