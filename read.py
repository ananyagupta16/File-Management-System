import os

def read_file(file_name):
    try:
        with open('Caption.txt', 'r') as f:
            content = f.read()
            print(f"Content of {file_name} : \n{content}")

    except FileNotFoundError:
        print(f"{file_name} doesn't exist!")

    except Exception as e:
        print("An error occured!")