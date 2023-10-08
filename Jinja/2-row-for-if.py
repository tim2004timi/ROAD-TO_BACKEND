from jinja2 import Template


data = """\
{% raw %}Jinja место определения {{ name }}
подставляет соответствующее значение{% endraw %}
"""

tp = Template(data)
message = tp.render(name="Tim")

print(message)

# -------------------------------------------------

link = "HTML <a href='#'>Ссылка</a>"

tp = Template("{{ link | e }}")
message = tp.render(link=link)

print(message)

# -------------------------------------------------

cities = [
    {"id": 1, "city": "Moscow"},
    {"id": 2, "city": "Taganrog"},
    {"id": 3, "city": "Sochi"}
]

text = """\
<select name="cities">
{% for city in cities -%}
{% if city.id > 0 -%}
    <option value="{{ city.id }}">{{ city.city }}</option>
{% endif -%}
{% endfor -%}
</select>
"""

tp = Template(text)
message = tp.render(cities=cities)

print(message)
