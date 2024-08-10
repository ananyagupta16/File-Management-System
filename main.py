from create import create_file
from view import view_all_files
from delete import delete_file
from read import read_file
from edit import edit_file
from rename import rename_file
from search import search_file

def main():
    while True:
        print("MINI FILE MANAGEMENT APP \n")
        print('Press 1: Create file')
        print('Press 2: View files in the current directory')
        print('Press 3: Delete file')
        print('Press 4: Read file')
        print('Press 5: Edit file')
        print('Press 6: Rename file')
        print('Press 7: Search file')
        print('Press 8: Exit')

        choice = input("Enter your choice(From 1 to 8): ")

        if choice == '1':
            file_name = input("Enter the file name to create: ")
            create_file(file_name)
        
        elif choice =='2':
            view_all_files()

        elif choice =='3':
            file_name = input("Enter the file name you want to delete: ")
            delete_file(file_name)

        elif choice == '4':
            file_name = input("Enter the file name you want to read: ")
            read_file(file_name)

        elif choice == '5':
            file_name = input("Enter the file name you want to edit: ")
            edit_file(file_name)

        elif choice == '6':
            old_name = input("Enter the current file name: ")
            new_name = input("Enter the new file name: ")
            rename_file(old_name, new_name)

        elif choice == '7':
            file_name = input("Enter the file name to search for: ")
            search_file(file_name)

        elif choice == '8':
            print("Closing the app...")
            break
        
        else:
            print("In-valid syntax, please try again.")

#calling main() function
main()
