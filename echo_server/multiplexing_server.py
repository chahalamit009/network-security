import socket,select,sys,Queue
#basic opening of socket creation
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to make the socket resuable
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#to make the socket not to block incoming connection
tcpSocket.setblocking(0)
#bind ip and port (values as tuples)
tcpSocket.bind(("0.0.0.0",8000))
#how many clients can connect at a time
tcpSocket.listen(5)

print "Waiting for a Client ...."
holeinsock = []

while True:
        read, write, ex = select.select([tcpSocket]+ holeinsock, [], [])
        for sig in read:
            if sig is tcpSocket:
                (client, (ip, port)) = tcpSocket.accept()
                print "Received a connection from IP %s on port %s"% (ip,port)
                print "Starting ECHO output..."
                holeinsock.append(client)
            else :
                data = sig.recv(1024)
                if not data:
                    holeinsock.remove(sig)
                    print "Closing connection..."
                    sig.close()
                else:
                    print "Received this from IP %s on port %s: %s"% (ip,port,data)
                    client.send(data)
