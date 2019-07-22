#Alvin Nguyen 28864658
#Farnaz Safaei Takhtehfoulad 73932218
#
#Project 2
#

import socket
import connectfourshared

def user_host() -> str:
    """Obtain a user input of the host/IP address name"""
    while True:
        host = input("Enter your host: ").strip()

        if len(host) == 0:
            print("Please re-enter your host name or IP address")
        else:
            return host

def user_port() -> int:
    """Obtain a user input of the port number"""
    while True:
        try:
            port = int(input("Enter your port #: ").strip())

            if port < 0 or port > 65535:
                print("Please re-enter port number")
            else:
                return port
            
        except ValueError:
                print("Ports must be an integer between 0 and 65535")
             
def connect_to_four(user_host: str, user_port: int, user_socket: "socket") -> "connection":
    """Connects to the desired server using the sockets, and interprets
       client input as read by the server, and server output
       as string output"""
    user_socket.connect((user_host, user_port))

    user_socket_input = user_socket.makefile("r")
    user_socket_output = user_socket.makefile("w")

    return user_socket, user_socket_input, user_socket_output

def close_connection(connection: "connection") -> None:
    """Closes the connection to the server"""
    user_socket, user_socket_input, user_socket_output = connection

    user_socket_input.close()
    user_socket_output.close()
    user_socket.close()

def send_message(connection: "connection", message: str) -> None:
    """Sends the string message of the client to the server"""

    user_socket, user_socket_input, user_socket_output = connection

    user_socket_output.write(message + "\r\n")
    user_socket_output.flush()

def receive_response(connection: "connection") -> None:
    """Receives the message sent by the server to the client"""
    user_socket, user_socket_input, user_socket_output = connection
    return user_socket_input.readline()[:-1]
    
def user_connect() -> "connection":
    """Executes the functions to connect to the server, or close the connection
       if a failure occurs."""
    host = user_host()
    port = user_port()
    user_socket = socket.socket()
    print("Connecting to {} (port {})...".format(host, port))
    
    try:
        connection = connect_to_four(host, port, user_socket)
        print("Connected!")
        return connection
    except:
        user_socket.close()
        return None


