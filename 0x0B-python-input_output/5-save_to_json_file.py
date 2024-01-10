#!/usr/bin/python3
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

file_name = input("Enter the name of the file you want to read: ")
json_string = read_file(file_name)

if json_string:
    python_object = from_json_string(json_string)
    if python_object:
        print("The content of the file is:", python_object)
    else:
        print("Converting the JSON string to a Python object failed.")
else:
    print("Reading the file failed.")
