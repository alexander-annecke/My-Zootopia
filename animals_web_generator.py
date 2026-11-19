import json

def load_data(file_path):
    """ Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


for animal in animals_data:
    characteristics = animal.get("characteristics", {})

    print(f'Name: {animal.get("name", "Unknown")}')
    print(f'Diet: {characteristics.get("diet", "Unknown")}')
    print(f'Location: {animal.get("locations", ["Unknown"])[0]}')
    print(f'Type: {characteristics.get("type", "Unknown")}')
    print()