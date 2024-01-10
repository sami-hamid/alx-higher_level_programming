#!/usr/bin/python3
import json

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("File written successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def to_json_string(python_object):
    try:
        json_string = json.dumps(python_object)
        return json_string
    except Exception as e:
        print("An error occurred:", str(e))
        return None

file_name = input("Enter the name of the file you want to write: ")
content = input("Enter the content you want to write to the file: ")
json_string = to_json_string(content)

if json_string:
    write_file(file_name, json_string)
else:
    print("Converting the content to a JSON string failed.")
