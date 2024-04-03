# CS5700
# Assignment 1
# Yiming Ge

# This is the TCP server which will create a string containing its name 
# and then begin accepting connections from clients
# It will prints out serveral info simialr as clients terminal

import socket
from socket import timeout
import threading

# server_ip = "127.0.0.1"  # local test ip
server_ip = "10.0.0.40"
server_port = 12000      # a server port larger than 5000
server_integer = 27     # fixed server integer
server_name = "Yiming Ge"
server_response_message = "{},{}".format(server_name, server_integer) # message will be sent back to client

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
server_socket.settimeout(1) # Set timeout to 1 second
print("The server is ready to receive!")
print("The server with ip: {} and port: {}".format(server_ip, server_port))

# This is the function to check whether the given string is integer
def is_integer(number):
    flag = True
    try:
        int(number)
    except ValueError:
        flag = False
    return flag

# This Function will handle the client connection
def handle_client(connection_socket, addr):
    global server_running
    try:
        # receive message from the client
        message = connection_socket.recv(1024).decode()
        client_name, client_integer = message.split(',')

        # Check if client given integer is integer and in the range.
        if is_integer(client_integer) and 1 <= int(client_integer) <= 100:
            client_integer = int(client_integer)
            total_integer = client_integer + server_integer
            # Send server response message back to the client
            connection_socket.send(server_response_message.encode())
            # Display the info on the terminal
            print("Client Name: Client of {}".format(client_name))
            print("Server Name: Server of {}".format(server_name))
            print("Client Integer Value: {}".format(client_integer))
            print("Server Integer Value: {}".format(server_integer))
            print("The Sum: {}".format(total_integer))
        else:
            print("Received out-of-range integer, shutting down.")
            connection_socket.send("Given not valid integer, Server shutting down.".encode())
            server_running = False
    except Exception as err:
        print(f'Exception caught: {err}\nClosing...')
    finally:
        # Closing the client socket
        connection_socket.close()

# Multi threads
server_running = True
try:
    while server_running:
        try:
            connection_socket, addr = server_socket.accept()
            print("Successfully connected the client with ip: {} and port: {} ".format(addr[0], addr[1]))
        except timeout:
            continue  # Timeout occurred, loop back and check server_running
        except OSError:
            break  # Handle case where server_socket gets closed
        # Start a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(connection_socket, addr))
        client_thread.start()


except KeyboardInterrupt:
    print("Ctrl+C pressed... Shutting Down")
except Exception as err:
    print(f'Exception caught: {err}\nClosing...')
finally:
    # Close the server socket
    server_socket.close()
