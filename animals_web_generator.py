import json

def load_data(file_path):
    """ Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


output = ''
for animal in animals_data:
    characteristics = animal.get("characteristics", {})

    output += f'Name: {animal.get("name", "Unknown")}\n'
    output += f'Diet: {characteristics.get("diet", "Unknown")}\n'
    output += f'Location: {animal.get("locations", ["Unknown"])[0]}\n'
    output += f'Type: {characteristics.get("type", "Unknown")}\n'

print(output)

with open("animals_template.html", "r", encoding="utf-8") as handle:
    template = handle.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)