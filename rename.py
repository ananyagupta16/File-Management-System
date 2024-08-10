import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully!")
    except FileNotFoundError:
        print(f"File '{old_name}' doesn't exist!")
    except Exception as e:
        print(f"An error occurred: {e}")