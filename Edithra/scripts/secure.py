# Security Hardening Script
import os

def disable_debug():
    """Ensures DEBUG mode is off in production."""
    env_path = "Edithra/.env"
    with open(env_path, "r") as file:
        lines = file.readlines()

    with open(env_path, "w") as file:
        for line in lines:
            if line.startswith("DEBUG="):
                file.write("DEBUG=False\n")
            else:
                file.write(line)

    print("🔒 DEBUG Mode Disabled!")

if __name__ == "__main__":
    disable_debug()




