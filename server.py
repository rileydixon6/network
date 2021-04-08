import socketserver
import socket
users = {}



class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """



    def handle(self):
        name = self.request.recv(1024).strip()
        users[name] = self.request
        while True:
            # self.request is the TCP socket connected to the client
            data = self.request.recv(1024).strip()
            
            if len(data) == 0:
                print("Disconnecting")
                break
            print("{} wrote:".format(name))
            print(data)
            # just send back the same data, but upper-cased
            tosend = self.request.recv(1024).strip()
            users[tosend].sendall(bytes("From {}: {}".format(name,data),encoding='utf8'))
            

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "10.15.12.245", 9999


    # Create the server, binding to localhost on port 9999
    with ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()