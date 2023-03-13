import json
import time

"""data = open('test.json', 'r').read()
user_info = json.loads(data)
user_info['users'].append({'username': 'tayven_wins','password': 'password3', 'user_id': 837143})
user_info_json = json.dumps(user_info, separators=(',', ':'), indent=5)
open('test.json', 'w').write(user_info_json)"""

# {123123: ['test_username', 'test_password']}
sample_data = [123123, ['test_username', 'test_password']]
sample_json_structure = {'users': {}}


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


#update_json_file('userdata.json', 'users', sample_data)


configure_json_file('userdata.json', sample_json_structure)