#!/usr/bin/python3
""" A module that converts attributes to dictionary"""
import sys

if __name__ == "__main__":

    save_to_json_file =__import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    add_args = load_from_json_file("add_item.json")

except FileNotFoundError:

    add_args = []

    add_args.extend(sys.argv[1:])
    save_to_json_file(add_args, "add_item.json")
