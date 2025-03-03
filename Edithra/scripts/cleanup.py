# Cleanup Script
import os
import shutil

def clear_logs():
    """Deletes all logs and temporary files."""
    log_dirs = ["Edithra/logs", "Edithra/tmp"]
    for dir_path in log_dirs:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)
            print(f"🧹 Cleared: {dir_path}")

if __name__ == "__main__":
    clear_logs()




