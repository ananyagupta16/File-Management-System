import os

def search_file(file_name):
    files = os.listdir()
    if file_name in files:
        print(f"File '{file_name}' found in the directory!")
    else:
        print(f"File '{file_name}' not found!")