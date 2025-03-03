import os

def restore_project(backup_file="edithra_project_final_backup_optimized.txt", overwrite=True):
    """
    Restores project files from the optimized backup text file.

    Parameters:
    - backup_file (str): The backup file path.
    - overwrite (bool): If True, overwrites existing files; if False, skips existing files.
    """

    if not os.path.exists(backup_file):
        print("❌ Backup file not found! Ensure it's in the project directory.")
        return

    with open(backup_file, "r", encoding="utf-8") as backup:
        lines = backup.readlines()

    current_file = None
    file_content = []

    for line in lines:
        if line.startswith("### FILE: "):
            # Write the previous file before moving to the next
            if current_file:
                if not os.path.exists(current_file) or overwrite:
                    os.makedirs(os.path.dirname(current_file), exist_ok=True)
                    with open(current_file, "w", encoding="utf-8") as f:
                        f.writelines(file_content)
                    print(f"✅ Restored: {current_file}")
                else:
                    print(f"⏩ Skipped (exists): {current_file}")

            # Extract new file path
            current_file = line.strip().replace("### FILE: ", "")
            file_content = []
        else:
            file_content.append(line)

    # Ensure the last file is written
    if current_file:
        if not os.path.exists(current_file) or overwrite:
            os.makedirs(os.path.dirname(current_file), exist_ok=True)
            with open(current_file, "w", encoding="utf-8") as f:
                f.writelines(file_content)
            print(f"✅ Restored: {current_file}")
        else:
            print(f"⏩ Skipped (exists): {current_file}")

    print("\n🎉 Edithra Project Restored Successfully!")

if __name__ == "__main__":
    restore_project(overwrite=True)  # Change to False to skip existing files
