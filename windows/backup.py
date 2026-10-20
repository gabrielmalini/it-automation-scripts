# Script Name: backup.py
# Purpose: Automate directory backup with timestamp (Windows)
# Author: Gabriel Malini Rodrigues
# Module: SWE4303 - Computing Infrastructure
#
# HOW TO RUN (Windows):
#   1. Open Command Prompt (no admin needed)
#   2. Navigate to the folder: cd C:\path\to\this\file
#   3. Run: python backup.py
#
# REQUIREMENTS:
#   - Python 3.x installed (https://www.python.org/downloads/)
#   - No extra libraries needed (uses only built-in modules)

import os
import shutil
import datetime

def create_backup(source_dir, dest_dir):
    """
    Create a compressed ZIP backup of source_dir inside dest_dir.
    The backup filename includes a timestamp so it is unique every run.

    Parameters:
        source_dir (str): The folder you want to back up.
        dest_dir   (str): The folder where backups will be saved.
    """

    # Step 1: Make sure the destination/backup folder exists
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Backup destination folder: {dest_dir}")

    # Step 2: Build a timestamp string  e.g. 2025-05-15_14-30-00
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Step 3: Build the full path for the backup archive (without extension)
    #         shutil.make_archive will add '.zip' automatically
    backup_name = f"backup_{timestamp}"
    backup_base = os.path.join(dest_dir, backup_name)   # no .zip yet

    # Step 4: Create the compressed ZIP archive
    print(f"\nCreating compressed backup of: {source_dir}")
    archive_path = shutil.make_archive(
        base_name=backup_base,   # path + filename prefix
        format="zip",            # creates a .zip file
        root_dir=source_dir      # folder to compress
    )

    # Step 5: Report success
    size_mb = os.path.getsize(archive_path) / (1024 * 1024)
    print(f"\n[SUCCESS] Backup completed successfully.")
    print(f"  Backup file : {archive_path}")
    print(f"  File size   : {size_mb:.2f} MB")
    return archive_path

def main():
    print("=" * 55)
    print("  Automated Backup Script (Python - Windows)")
    print("=" * 55)

    # --- Get the currently logged-in local account info ---
    # os.environ['USERNAME']    -> current account username (e.g. jsmith)
    # os.environ['USERPROFILE'] -> current account home path (e.g. C:\Users\jsmith)
    # This always reflects the LOCAL account running the script,
    # NOT the main administrator account.
    current_user = os.environ.get('USERNAME', 'UnknownUser')
    user_profile = os.environ.get('USERPROFILE', '')

    print(f"\n  Running as user: {current_user}")

    # --- CONFIGURE THESE TWO PATHS ---
    # SOURCE: the directory where this script is located
    source = os.path.dirname(os.path.abspath(__file__))

    # DEST: where the backup ZIP files will be saved
    dest = os.path.join(user_profile, "backup_folder")     # e.g. C:\Users\jsmith\backup_folder
    # ---------------------------------

    # Validate source exists
    if not os.path.isdir(source):
        print(f"\n[ERROR] Source folder does not exist: {source}")
        print("  Please edit the 'source' variable at the top of main() to a valid path.")
        return

    print(f"\n  Source folder : {source}")
    print(f"  Backup folder : {dest}")

    # Run the backup
    create_backup(source, dest)

    print("\nScript execution completed.")
    print("=" * 55)

if __name__ == "__main__":
    main()
