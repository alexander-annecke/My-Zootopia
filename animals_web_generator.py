import json


def load_data(file_path):
    """Lädt eine JSON-Datei und gibt ihren Inhalt zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Erstellt das HTML für ein einzelnes Tier."""
    characteristics = animal_obj.get("characteristics", {})
    taxonomy = animal_obj.get("taxonomy", {})
    locations = animal_obj.get("locations", [])

    location_text = " and ".join(locations) if locations else "Unknown"
    animal_type = characteristics.get("type") or taxonomy.get("class", "Unknown")

    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
        '  <p class="card__text">\n'
        f'    <strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br/>\n'
        f'    <strong>Location:</strong> {location_text}<br/>\n'
        f'    <strong>Type:</strong> {animal_type}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )


def main():
    animals_data = load_data("animals_data.json")

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html)


if __name__ == "__main__":
    main()