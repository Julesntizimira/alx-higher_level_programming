#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from typing import List


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

def add_items_to_list(args: List[str]) -> List[str]:
    try:
        existing_items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_items = []

    updated_items = existing_items + args
    save_to_json_file(updated_items, 'add_item.json')

    return updated_items

if __name__ == '__main__':
    args = sys.argv[1:]
    added_items = add_items_to_list(args)
    print(f"Items added: {', '.join(added_items)}")
