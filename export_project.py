import os

# Define the root directory of your project
root_dir = "/workspaces/Edithra"  # Change this path if needed
output_file = "project_backup.txt"

def export_project(root, output):
    with open(output, "w", encoding="utf-8") as f:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file_content:
                        content = file_content.read()
                        f.write(f"## FILE: {file_path}\n")
                        f.write(content + "\n\n")
                except Exception as e:
                    f.write(f"## FILE: {file_path} (Error reading: {e})\n\n")

export_project(root_dir, output_file)
print(f"✅ All files copied! Check {output_file}")


