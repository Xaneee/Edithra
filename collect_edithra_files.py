import os

# Define the root directory of the project
root_directory = "./Edithra"  # Change if needed
output_file = "edithra_project_backup.txt"

# Open the output file
with open(output_file, "w", encoding="utf-8") as backup:
    
    # Walk through all directories and files
    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Write the file path
            backup.write(f"## FILE: {file_path}\n")
            
            # Read the file content and write it
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                backup.write(f.read())
            
            # Add spacing for clarity
            backup.write("\n\n" + "="*80 + "\n\n")

print(f"✅ Project backup saved to {output_file}")
