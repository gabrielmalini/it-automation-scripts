# Script Name: create_user.py
# Purpose: Create a new Windows local user and assign permissions
# Author: Gabriel Malini Rodrigues
# Module: SWE4303 - Computing Infrastructure
#
# HOW TO RUN (Windows):
#   1. Open Command Prompt AS ADMINISTRATOR (right-click > Run as administrator)
#   2. Navigate to the folder: cd C:\path\to\this\file
#   3. Run: python create_user.py
#
# REQUIREMENTS:
#   - Python 3.x installed (https://www.python.org/downloads/)
#   - Must run as Administrator

import subprocess
import sys
import os

def check_admin():
    """Check if the script is running with administrator privileges."""
    try:
        result = subprocess.run(
            ["net", "session"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False

def user_exists(username):
    """Check if a Windows local user account already exists."""
    result = subprocess.run(
        ["net", "user", username],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def create_user(username, password):
    """Create a new Windows local user with the given username and password."""
    result = subprocess.run(
        ["net", "user", username, password, "/add"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout + result.stderr

def create_shared_folder(username):
    """Create a private shared folder for the user and set permissions."""
    folder_path = os.path.join("C:\\Users", username, "shared_folder")

    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created: {folder_path}")

    # Set permissions: only the owner (user) has full access
    # /inheritance:r  removes inherited permissions
    # /grant gives the specific user full control (F)
    subprocess.run(
        ["icacls", folder_path, "/inheritance:r", "/grant", f"{username}:(F)"],
        capture_output=True,
        text=True
    )
    print(f"Permissions set: Only '{username}' has full access to {folder_path}")
    return folder_path

def main():
    print("=" * 50)
    print("  User Account Creation Script (Python - Windows)")
    print("=" * 50)

    # Step 1: Check for admin rights
    if not check_admin():
        print("\n[ERROR] This script must be run as Administrator.")
        print("  Right-click Command Prompt > 'Run as administrator'")
        sys.exit(1)

    # Step 2: Get username input
    username = input("\nEnter the username to create: ").strip()

    if not username:
        print("[ERROR] Username cannot be empty.")
        sys.exit(1)

    # Step 3: Check if user already exists
    if user_exists(username):
        print(f"\n[INFO] User '{username}' already exists on this system.")
    else:
        # Step 4: Get password
        password = input(f"Enter a password for '{username}': ").strip()

        if not password:
            print("[ERROR] Password cannot be empty.")
            sys.exit(1)

        # Step 5: Create the user
        success, message = create_user(username, password)
        if success:
            print(f"\n[SUCCESS] User '{username}' created successfully.")
        else:
            print(f"\n[ERROR] Failed to create user: {message}")
            sys.exit(1)

        # Step 6: Create shared folder and set permissions
        folder = create_shared_folder(username)
        print(f"\n[SUCCESS] Shared folder created at: {folder}")
        print(f"[SUCCESS] Permissions assigned: '{username}' has full access only.")

    print("\nScript execution completed.")
    print("=" * 50)

if __name__ == "__main__":
    main()
