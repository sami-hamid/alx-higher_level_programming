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

def append_after(data, item_to_append, after_item):
    try:
        index = data.index(after_item)
        data.insert(index + 1, item_to_append)
        return data
    except ValueError:
        print("The item after which to append is not in the list.")
        return None

file_name = input("Enter the name of the file you want to read: ")
json_string = read_file(file_name)

if json_string:
    python_object = from_json_string(json_string)
    if python_object:
        if isinstance(python_object, list):
            item_to_append = input("Enter the item you want to append: ")
            after_item = input("Enter the item after which to append: ")

            new_data = append_after(python_object, item_to_append, after_item)
            if new_data:
                print("The new data is:", new_data)
            else:
                print("Appending the item failed.")
        else:
            print("The content of the file is not a list.")
    else:
        print("Converting the JSON string to a Python object failed.")
else:
    print("Reading the file failed.")
