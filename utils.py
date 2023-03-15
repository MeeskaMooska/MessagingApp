import json



def configure_json_file(path, structure):
    with open(path, 'w') as file:
        file.write(json.dumps(structure, separators=(',', ':'), indent=5))


def collect_json_from_file(path):
    with open(path, 'rt') as file:
        return json.loads(file.read())


def update_json_file(path, location, data):
    updated_file_data = collect_json_from_file(path)[location][data[0]] = data[1]
    with open(path, 'w') as file:
        file.write(json.dumps(updated_file_data, separators=(',', ':'), indent=5))
