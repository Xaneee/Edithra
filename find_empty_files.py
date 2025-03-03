import os

def find_empty_files(directory="."):
    """
    Finds all empty files in the specified directory and its subdirectories.
    
    Parameters:
    - directory (str): The root directory to search.
    """
    empty_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                empty_files.append(file_path)

    if empty_files:
        print("\n📂 Empty Files Found:")
        for file in empty_files:
            print(f"❌ {file}")
    else:
        print("\n✅ No empty files found!")

    return empty_files

if __name__ == "__main__":
    project_directory = os.getcwd()  # Set to project root
    find_empty_files(project_directory)
