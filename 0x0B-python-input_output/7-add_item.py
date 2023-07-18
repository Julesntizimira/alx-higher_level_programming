#!/usr/bin/python3
''' scripts to add arguments to a list and
    save them to json file
'''
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
length = len(argv)
j = 0
for i in range(length):
    if j == 0:
        j += 1
        continue
    my_list.append(argv[i])

with open('add_item.json', 'w') as f:
    json.dump(my_list, f)
