#!/usr/bin/python3

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("File written successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

file_name = input("Enter the name of the file you want to write: ")
content = input("Enter the content you want to write to the file: ")
write_file(file_name, content)
