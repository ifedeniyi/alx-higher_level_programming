#!/usr/bin/python3
"""Appends command-line args to json file."""
import sys
from pathlib import Path

stojson = __import__("5-save_to_json_file").save_to_json_file
lfromjson = __import__("6-load_from_json_file").load_from_json_file

old_obj = []
new_obj = sys.argv[1:]

if Path.is_file(Path.cwd() / 'add_item.json'):
    old_obj = lfromjson("add_item.json")

stojson([*old_obj, *new_obj], "add_item.json")
