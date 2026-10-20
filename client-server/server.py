# server.py
# Simple TCP Server that sends system time to client
# Module: SWE4303 - Computing Infrastructure
# Author: Gabriel Malini Rodrigues
#
# HOW TO RUN (Windows):
#   1. Open Command Prompt
#   2. Navigate to the folder: cd C:\path\to\this\file
#   3. Run: python server.py
#   4. THEN open a second Command Prompt and run: python client.py
#
# REQUIREMENTS:
#   - Python 3.x installed
#   - No extra libraries needed

import socket
import datetime

def start_server():
    # Create a TCP socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of the port immediately after the server closes
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Define host and port
    host = "127.0.0.1"   # localhost - only accepts connections from this machine
    port = 5000

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening - allow up to 1 queued connection
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port} ...")
    print("Waiting for a client to connect...")

    # Accept a client connection (this blocks until a client connects)
    conn, addr = server_socket.accept()
    print(f"\n[CONNECTED] Client connected from: {addr}")

    # Get the current system time as a formatted string
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Send the time to the client (must encode string to bytes)
    conn.send(current_time.encode())
    print(f"[SENT] System time sent to client: {current_time}")

    # Close the connection and socket
    conn.close()
    server_socket.close()
    print("[INFO] Connection closed. Server stopped.")

if __name__ == "__main__":
    start_server()
