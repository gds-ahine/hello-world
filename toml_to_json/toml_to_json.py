import toml
import json

toml_file = toml.load('accounts_loggroup_index.toml')

with open('accounts_loggroup_index.json', 'w') as json_file:
	json_file.write(json.dumps(toml_file))
