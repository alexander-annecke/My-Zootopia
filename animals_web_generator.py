import json

def load_data(file_path):
    """ Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

data = load_data("animals_data.json")


output = ""

for animal_data in data:
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_data["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal_data["characteristics"].get("diet", "Unknown")}<br/>\n'
    output += f'      <strong>Location:</strong> {animal_data["locations"][0]}<br/>\n'
    output += f'      <strong>Type:</strong> {animal_data["characteristics"].get("type", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

print(output)

with open("animals_template.html", "r", encoding="utf-8") as handle:
    template = handle.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)