import socket
import threading
def listen_client(client,address):
    data='dummy'
    ip,port = address
    print "Received connection from : ", ip

    print "Starting ECHO output................"
    while len(data):
        data = client.recv(2048)
        print "Client"+str(ip)+":"+str(port)+" sent : "+data
        client.send(data)

    print "Closing connection ..."
    client.close()
#basic opening of socket creation
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to make the socket resuable
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind ip and port (values as tuples)
tcpSocket.bind(("0.0.0.0",8000))
#how many clients can connect at a time
tcpSocket.listen(5)

print "Waiting for a Client ...."
while True:
    (client, ( ip, sock)) = tcpSocket.accept()
    client.settimeout(120)
    threading.Thread(target=listen_client,args=(client,(ip,sock))).start()

print "Shutting down server ..."
tcpSocket.close()
