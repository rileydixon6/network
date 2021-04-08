import socket
import sys
import threading

HOST, PORT = "10.15.12.245", 9999

def recieve_message():
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    messages = threading.Thread(target=recieve_message)
    messages.start()
    name = input("Please enter your name: ")
    sock.sendall(bytes(name + "\n", "utf-8"))
    data = input()
    tosend = input("to: ")
    
    while data != "end":
        
        sock.sendall(bytes(data + "\n", "utf-8"))
        sock.sendall(bytes(tosend + "\n", "utf-8"))
        data = input()
        tosend = input("to: ")
