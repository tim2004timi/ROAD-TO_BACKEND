import re


text = "+7(123)456-78-90"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}",text)
print(m)

new_string = re.sub(r"(\d+)", r"|\1|", text)
print(new_string)

text = """Hello, my name is Tim! I am codding now
and soon I will go to the university.
I love Python
"""
lst = re.split(r"[\n!.,]", text)
print(lst)
