import re


text = "<p>Image <img src='bg.jpg'> in text</p>"

match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)>", text)
print(match)

# (?:) - несохраняющая группировка
# () - сохраняющая группировка
# (?P<name>) - дать название группе
# (?P=name) - обратиться к группе
