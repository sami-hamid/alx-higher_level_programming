#!/usr/bin/python3
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print("An error occurred:", str(e))

file_name = input("Enter the name of the file you want to read: ")
read_file(file_name)
