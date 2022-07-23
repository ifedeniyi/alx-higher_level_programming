#!/usr/bin/python3
"""Appends commandline args to json file"""
import sys
import os
from pathlib import Path

stojson = __import__("5-save_to_json_file").save_to_json_file
lfromjson = __import__("6-load_from_json_file").load_from_json_file
args = sys.argv[1:]

final_obj = []

if Path.is_file(Path.cwd() / 'add_item.json'):
    final_obj = lfromjson("add_item.json")

stojson([*final_obj, *args], "add_item.json")
