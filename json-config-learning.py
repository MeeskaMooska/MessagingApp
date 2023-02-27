import json

data = open('test.json', 'r').read()
user_info = json.loads(data)
user_info['users'].append({'username': 'tayven_wins','password': 'password3', 'user_id': 837143})
user_info_json = json.dumps(user_info, separators=(',', ':'), indent=5)
open('test.json', 'w').write(user_info_json)