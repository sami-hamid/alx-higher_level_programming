#!/bin/bash/python3
def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("File written successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def append_write(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print("Content appended to the file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

file_name = input("Enter the name of the file you want to write: ")
content = input("Enter the content you want to write to the file: ")
write_or_append = input("Choose 'write' or 'append': ")

if write_or_append.lower() == 'write':
    write_file(file_name, content)
elif write_or_append.lower() == 'append':
    append_write(file_name, content)
else:
    print("Invalid input.")
