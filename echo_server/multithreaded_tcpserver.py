from SocketServer import ThreadingTCPServer, BaseRequestHandler
import threading

class EchoHandler(BaseRequestHandler):

    def handle(self):
        print "Got Connection from : ", self.client_address
        data = 'dummy'

        while len(data):
            data = self.request.recv(1024)
            self.request.send(data)

        print "Client left"

serverAddr = ("0.0.0.0", 8000)

server = ThreadingTCPServer(serverAddr, EchoHandler)
server.allow_reuse_address = True
server.serve_forever()
