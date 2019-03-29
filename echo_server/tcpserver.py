import SocketServer
import socket

class EchoHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "Got Connection from : ", self.client_address
        data = 'dummy'

        while len(data):
            data = self.request.recv(1024)
            self.request.send(data)

        print "Client left"

serverAddr = ("0.0.0.0", 8000)

server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()
