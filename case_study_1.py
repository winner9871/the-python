import os

def print_menu():
    print()
    print(os.getcwd())
    print("1 List the current directory")
    print("2 Move up")
    print("3 Move down")
    print("4 Number of files in the directory")
    print("5 Size of the directory in bytes")
    print("6 Search for a filename")
    print("7 Quit the program")

def get_folder_size(path="."):
    sep = os.sep
    size = 0
    print(os.listdir(path))
    for folder_content in os.listdir(path):
        if os.path.isfile(f"{path}{sep}{folder_content}"):
            size += os.path.getsize(f"{path}{sep}{folder_content}")
        else:
            size += get_folder_size(f"{path}{sep}{folder_content}")
    return size

def search_file(search_str, path= "."):
    sep = os.sep
    matched_cases = []
    folder_contents = os.listdir(path)
    matched_cases += [(path + sep + folder_content) for folder_content in folder_contents if search_str in folder_content]
    for folder_content in folder_contents:
        if os.path.isdir(path + sep + folder_content):
            matched_cases += search_file(search_str, path= (path + sep + folder_content))
    return matched_cases

def number_of_files(path="."):
    count = 0
    sep = os.sep
    folder_contents = os.listdir(path)
    for folder_content in folder_contents:
        if os.path.isdir(path + sep + folder_content):
            count += number_of_files(path= (path + sep + folder_content))
        else:
            count += 1
    return count

def main():
    sep = os.sep
    while True:
        print_menu()
        choice = input("Enter Number:\t")

        if choice == "1":
            print(os.getcwd())
        
        elif choice == "2":
            cwd = os.getcwd()
            parent = cwd[::-1].partition(sep)[-1][::-1]
            if parent != "":
                os.chdir(parent)
            else:
                print("Already at root")
        
        elif choice == "3":
            cwd_content = os.listdir()
            folders_in_cwd = [content for content in cwd_content if os.path.isdir(f".{sep}{content}")]
            print(folders_in_cwd)
            moveTo = input("Enter the name of dir you want to move:\t")
            if os.path.exists(f".{sep}{moveTo}"):
                os.chdir(f".{sep}{moveTo}")
            else:
                print(f"no dir name {moveTo}")
        
        elif choice == "4":
            print(number_of_files())

        elif choice == "5":
            print(get_folder_size("."))

        elif choice == "6":
            search_str = input("Enter Some text to search for those:\t")
            print(search_file(search_str=search_str))

        elif choice == "7":
            break

        else :
            print("Invalid choice")

if __name__ == "__main__":
    main()
