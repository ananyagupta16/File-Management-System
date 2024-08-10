import os

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} has been deleted successfully!")

    except FileNotFoundError:
        print("File not found")
    
    except Exception as e:
        print("An error occured!")