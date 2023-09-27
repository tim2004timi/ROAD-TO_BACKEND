import re


text = "<font color=#CC0000>"
match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)  # Match object

print(match.group(0, 1, 2))  # ('color=#CC0000', 'color', '#CC0000')
print(match.groups())  # ('color', '#CC0000')
print(match.span(0))  # (6, 19)
print(match.groupdict())  # {'key': 'color', 'value': '#CC0000'}
print(match.expand(r"\g<key>:\g<value>"))  # color:#CC0000

# search() - находит только первый шаблон
# finditer() - итератор объектов match
# findall() - список найденных шаблонов
