import os

def edit_file(file_name):
    try:
        with open('Caption.txt', 'a') as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print("Content added to {file_name} successfully!")

    except FileNotFoundError:
        print(f"{file_name} doesn't exist!")

    except Exception as e:
        print("An error occured!")