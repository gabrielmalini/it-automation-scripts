#!/bin/bash
# Script Name: backup.sh
# Purpose: Automate a compressed directory backup with a timestamp
# Author: Gabriel Malini Rodrigues
# Usage: ./backup.sh

# Define source and destination
SOURCE="$HOME"
DEST="$HOME/backup_folder"

# Create backup folder if it does not exist
mkdir -p "$DEST"

# Get current date and time
DATE=$(date +%Y-%m-%d_%H-%M-%S)

# Create compressed backup (excluding the backup folder itself)
tar -czvf "$DEST/backup_$DATE.tar.gz" --exclude="$DEST" "$SOURCE"

echo "Backup completed successfully."
echo "Backup file: $DEST/backup_$DATE.tar.gz"
