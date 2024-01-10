#!/bin/bash/python3
import json

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def from_json_string(json_string):
    try:
        python_object = json.loads(json_string)
        return python_object
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def calculate_stats(data):
    total = len(data)
    avg = sum(data) / total
    max_value = max(data)
    min_value = min(data)

    return {
        "total": total,
        "avg": avg,
        "max": max_value,
        "min": min_value
    }

file_name = input("Enter the name of the file you want to read: ")
json_string = read_file(file_name)

if json_string:
    python_object = from_json_string(json_string)
    if python_object:
        if isinstance(python_object, list):
            stats = calculate_stats(python_object)
            print("The stats of the file content are:", stats)
        else:
            print("The content of the file is not a list.")
    else:
        print("Converting the JSON string to a Python object failed.")
else:
    print("Reading the file failed.")
