# Квантификаторы
import re


text = "gogle, google, gooogle, gooooogle"
match = re.findall(r"go{,5}gle?", text)
print(match)


phone = "89045550751"
match = re.findall(r"8\d{10}", phone)
print(match)

# {0, 1} - ?
# {0,} - *
# {1,} - +

text = "стеклянный, стекляный"
match = re.findall(r"стеклянн?ый", text)
print(match)

text = "автор=Пушкин А.С.; цена = 200; год= 2004 "
match = re.findall(r".+?\s*=\s*[^; ]+", text)
print(match)

