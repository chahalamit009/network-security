import socket
#basic opening of socket creation
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to make the socket resuable
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind ip and port (values as tuples)
tcpSocket.bind(("0.0.0.0",8000))
#how many clients can connect at a time
tcpSocket.listen(2)

print "Waiting for a Client ...."
(client, ( ip, sock)) = tcpSocket.accept()

print "Received connection from : ", ip

print "Starting ECHO output................"

data='dummy'

while len(data):
    data = client.recv(2048)
    print "Client sent : ",data
    client.send(data)

print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()    
