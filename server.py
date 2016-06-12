import socket #import socket Python library
import sys #import OS related Python library
 

HOST = '' #What is the HOST?
PORT = 8888 #What is the PORT?

#Open a new IP socket for streaming
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

print 'Socket created' #Show feedback to user

#Try create the socket on the local host and specific port or handle an error if it fails
try:
    s.bind((HOST, PORT))
except socket.error as msg: 
    print 'Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete' #Show feedback to user

#Tell the new socket to start listening and allow up to 10 connections
s.listen(10)

print 'Magic Eight Ball now listening'

while 1:
    #wait for other clients to connect, when client connects create two new variables
    conn, addr = s.accept()
    print 'Connected to by: ' + addr[0] + ':' + str(addr[1])

s.close() #close the connection






