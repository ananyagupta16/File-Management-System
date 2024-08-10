import os

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in directory!")
        for file in files:
            print(file, "\n")