from jinja2 import Template


cars = [
    {"model": "BMW", "price": 7000},
    {"model": "Mercedes", "price": 7500},
    {"model": "Ford", "price": 4200}
]

text = "Total summ of cars: {{ cars | sum(attribute='price') }}"
tp = Template(text)
message = tp.render(cars=cars)

print(message)

# ------------------------------------------------

html = """\
{% macro input(name, value='', type='text', size=20) -%}
    <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
{%- endmacro -%}

<p>{{ input('username', size=100) }}</p>
<p>{{ input('password') }}</p>\
"""
tp = Template(html)
message = tp.render()

print(message)
