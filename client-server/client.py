# client.py
# Simple TCP Client that receives system time from server
# Module: SWE4303 - Computing Infrastructure
# Author: Gabriel Malini Rodrigues
#
# HOW TO RUN (Windows):
#   1. First, start the server in a separate Command Prompt: python server.py
#   2. Then open a NEW Command Prompt
#   3. Navigate to the folder: cd C:\path\to\this\file
#   4. Run: python client.py
#
# REQUIREMENTS:
#   - Python 3.x installed
#   - server.py must be running BEFORE you run this file

import socket

def connect_to_server():
    # Create a TCP socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's host and port (must match server.py)
    host = "127.0.0.1"
    port = 5000

    print(f"Connecting to server at {host}:{port} ...")

    # Connect to the server
    client_socket.connect((host, port))
    print("[CONNECTED] Successfully connected to server.")

    # Receive data from the server (up to 1024 bytes)
    data = client_socket.recv(1024)

    # Decode the bytes back to a string and display it
    print(f"\nServer Time: {data.decode()}")

    # Close the socket
    client_socket.close()
    print("\n[INFO] Connection closed.")

if __name__ == "__main__":
    connect_to_server()
