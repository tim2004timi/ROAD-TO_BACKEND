import re


text = "еда, победа, кеды, беда, (еда), Еду, Еда 64"
match = re.findall(r"\w", text)
print(match)
