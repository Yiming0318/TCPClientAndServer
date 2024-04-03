# CS5700
# Assignment 1
# Yiming Ge


# This is the TCP client which send a message containing
# (i) a string containing your name
# (ii) the entered integer value
# and then wait for a sever reply.
# it will read the message sent by the server and display its name,
# the server’s name, its integer value, and the server’s integer value,
# and then compute and the sum.
# The client then terminates after releasing any created sockets

import socket
# Server IP and port which the client will send the request
# server_ip = "127.0.0.1"  # local test ip
server_ip = "10.0.0.40"
server_port = 12000      # a server port larger than 5000

# Client input
client_name = input("Please enter your name: ")
client_integer = input("Please enter one integer between 1 and 100: ")

# create TCP socket for server, remote port 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# combine the input as a string message name,integer
message = "{},{}".format(client_name, client_integer)

# Send message to the server
# converting the server_response string into
# a sequence of bytes (using UTF-8 encoding by default)
client_socket.send(message.encode())

# Receive the server response
server_response = client_socket.recv(1024).decode()
# Get the name and integer from server
server_name, server_integer = server_response.split(',')

try:
    server_integer = int(server_integer)
    client_integer = int(client_integer)
    # calculate the sum
    total_integer = client_integer + server_integer
    # Display info on the terminal
    print("Client Name: Client of {}".format(client_name))
    print("Server Name: Server of {}".format(server_name))
    print("Client Integer Value: {}".format(client_integer))
    print("Server Integer Value: {}".format(server_integer))
    print("The Sum: {}".format(total_integer))
except ValueError:  # handle invalid integer condition
    print("Given not valid integer, Server shutting down.")
finally:
    # Close the client socket
    client_socket.close()
