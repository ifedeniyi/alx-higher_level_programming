#!/usr/bin/python3
""""""
import sys
stojson = __import__("5-save_to_json_file").save_to_json_file
lfromjson = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]
# args = lfromjson(1)
stojson(args, "add_item.json")
sys.stdin
