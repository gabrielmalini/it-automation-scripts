#!/bin/bash
# Script Name: create_user.sh
# Purpose: Create a new Linux user and a private shared folder
# Author: Gabriel Malini Rodrigues
# Usage: sudo ./create_user.sh

# Ask for username
echo "Enter the username to create:"
read username

# Check if user already exists
if id "$username" &>/dev/null; then
    echo "User $username already exists."
else
    # Create user with home directory
    sudo useradd -m "$username"
    echo "User $username created successfully."

    # Set password (prompted interactively, never stored in the script)
    sudo passwd "$username"

    # Create a shared directory for the user
    sudo mkdir -p "/home/$username/shared_folder"

    # Change ownership
    sudo chown "$username:$username" "/home/$username/shared_folder"

    # Set permissions 700 = full access for the owner only
    sudo chmod 700 "/home/$username/shared_folder"
    echo "Permissions set for $username."
fi

echo "Script execution completed."
