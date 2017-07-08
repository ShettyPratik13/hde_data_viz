import os, json
import pandas as pd

# Edit path to json files here
path_to_json = '/Users/pratikshetty/Work/workshops/Takeout/Searches'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
# print json_files

for js in json_files:
    with open(os.path.join(path_to_json, js)) as json_file:
        data = json.load(json_file)

        for i in range(len(data['event'])):
        	for k,v in data['event'][i]['query'].items():
        		if k=='query_text':
        			# print(v)
        			with open('searchTerms', 'a') as f:
    					f.write(v.encode('utf-8') + '\n')


