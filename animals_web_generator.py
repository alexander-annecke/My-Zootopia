import json

def load_data(file_path):
    """ Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

data = load_data("animals_data.json")


output = ""

for animal_data in data:
    characteristics = animal_data.get("characteristics", {})
    locations = animal_data.get("locations", [])

    output += '<li class="cards__item">'
    output += f"Name: {animal_data.get('name', 'Unknown')}<br/>\n"
    output += f"Diet: {characteristics.get('diet', 'Unknown')}<br/>\n"
    output += f"Location: {locations[0] if locations else 'Unknown'}<br/>\n"
    output += f"Type: {characteristics.get('type', 'Unknown')}<br/>\n"
    output += "</li>\n"

print(output)

with open("animals_template.html", "r", encoding="utf-8") as handle:
    template = handle.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)