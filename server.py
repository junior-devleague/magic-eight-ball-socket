import socket #import socket Python library, socket is a single class
import sys #import OS related Python library, sys is a single class
from thread import *  #import all functions from the thread library by their own name

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

#create a function to talk to new client connections
def clientthread(conn):
    #Send a message back to the user that connected over this socket connection
    conn.send('You have summoned the Magic Eight Ball, what is your question?\n')
    
    while True:

        #Receive new messages from the client
        data = conn.recv(1024)
        reply = 'You asked: ' + data
        if not data:
            break

        conn.sendall(reply)

    conn.close() #close only this connection
        


while 1:
    #wait for other clients to connect, when client connects create two new variables
    conn, addr = s.accept()
    print 'Connected to by: ' + addr[0] + ':' + str(addr[1])

    start_new_thread(clientthread, (conn,))

s.close() #close the connection
