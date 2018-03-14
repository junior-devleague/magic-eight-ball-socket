# magic-eight-ball-socket
Magic eight ball demo as a client/server socket exercise

### Objective
We will be using the **socket** network interface to enable communication between computers. One person will run the Magic 8-Ball server, which will listen for connections on their machine. You must create a client that can send questions to the Magic 8-Ball. Then, you must alter the server so that it replies to the client's question with a randomly selected prediction.

### Prerequisites 
Students must already be familiar with the following:
- Concept of "client" and "server"
- Handling user input

### Requirements
To complete this project you will need:
- Any text editor you like (gedit, nano, vi/vim)
- `server.py` (provided)

### Desired Outcome
At the completion of this exercise, students should understand:
- Socket connections and how to create them
- Ports
- How to communicate between two computers on the same local network

### Your Challenge
1. Download `server.py` from this repository.
2. Run `server.py` in a terminal. You should see a message indicating that it's listening for connections.
3. Create a `client.py` that connects to the server. Pay attention to what port the server is listening on.
4. `client.py` must take a user's question and send it to the server.
5. Alter `server.py` so that it sends an answer back to the client. 

### Resources
- [Python Socket Docs](https://docs.python.org/3/library/socket.html)
- [Socket](https://steelkiwi.com/blog/working-tcp-sockets/)
