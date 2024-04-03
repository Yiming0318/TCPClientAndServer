
Overview
This project implements a TCP client-server application in Python that demonstrates basic network programming concepts, including socket communication, concurrency with threading, and simple data exchange protocols.

Features
TCP Socket Communication: Establishes a TCP connection between client and server for reliable data transmission.
Concurrent Server: Utilizes Python's threading library to handle multiple client connections simultaneously, making the server concurrent.

Requirements
Python 3.x

Libraries Used
socket: For TCP communication.
threading: To enable the server to handle multiple client connections concurrently.

Server Configuration
IP Address: Configured to listen on a specific IP address. For local testing, use 127.0.0.1. For network testing, use the server's network IP address.
Port: Listens on port 12000 (configurable).
Concurrency: Uses the threading library to spawn a new thread for each client connection, allowing the server to manage multiple connections in parallel.


How to Run
Server Setup:
Run the server script first to start listening for client connections.
Use the command python server.py to start the server.
Client Setup:
Run the client script to connect to the server and initiate data exchange.
Use the command python client.py to start the client.
Follow the prompts to enter your name and an integer.

Testing
Local Testing: Use server_ip = "127.0.0.1" for both client and server scripts for local testing.
Remote Testing: For testing over a network, find the server's IP address using ifconfig (Unix/Linux) or ipconfig (Windows) and set server_ip in the client script to this address.

Note
Ensure the server script is running before starting the client script.
The server is configured to shut down if it receives an out-of-range integer (outside 1-100). This behavior is intended for demonstration purposes and can be modified as needed.