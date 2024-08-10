import os

def create_file(file_name):
    try:
        with open(file_name, 'x') as f: # Here 'x" will create the file as the user passes the file_name
            print(f"File Name {file_name}: Created successfully!")
    except FileExistsError:
        print(f"File Name {file_name} is already exists!")
    except Exception as E:
        print("An Error occurred!")