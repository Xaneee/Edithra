import os

# Define the output file
output_file = "Edithra.txt"

# List of file extensions to include (Python, Java, HTML, JS, Docker, Configs)
valid_extensions = {".py", ".java", ".html", ".js", ".css", ".json", ".yaml", ".yml", ".sh", ".env", ".conf", ".Dockerfile"}

def write_to_file(output_path):
    """ Recursively writes all files with valid extensions into Edithra.txt """
    with open(output_file, "w", encoding="utf-8") as out:
        for root, _, files in os.walk(output_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Skip non-code files
                if not any(file.endswith(ext) for ext in valid_extensions) and "Dockerfile" not in file:
                    continue
                
                try:
                    # Write file path as a header
                    out.write(f"\n{'='*80}\n")
                    out.write(f"📂 FILE: {file_path}\n")
                    out.write(f"{'='*80}\n\n")
                    
                    # Write file contents
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        out.write(f.read() + "\n\n")
                    
                    print(f"✅ Copied: {file_path}")
                except Exception as e:
                    print(f"❌ Failed to copy {file_path}: {e}")

# Run the script
write_to_file(os.getcwd())

print(f"\n🎉 All code files copied to {output_file} successfully!")


