# Import the required python components
import socket, select, sys
#Command for exiting system
QUITCOMMAND = "#quit"
#Port number is a constant
PORT = 3000
#Initilize buffersize
bufferSize = 4096

# Used to add prefix to messages before printing
msgPrefix = ''

# Implement a socket
def implementSocket(address):
    clientConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    clientConnection.connect((address, PORT))
    return clientConnection

#Validate user's command to run the client host
if len(sys.argv) < 2:
    # Print invalid commend and standard error
    print("Invalid command! Write into cmd: Python3 chatClient.py [hostIP address]", file = sys.stderr)
    # Exit system because of improper command
    sys.exit(1)

# Create a connection if user's command is correct
else:
    # Implement a socket 
    clientConnection = implementSocket(sys.argv[1])
    # Print success message
    print("Connected to server\n")

# Holds the list of connections
connectionList = [sys.stdin, clientConnection]

# Create an infinite loop
while True:
     #Waiting until ready for reading, wait until ready for writing, wait for an "exceptional condition"
    userRead, userWrite, socketErr = select.select(connectionList, [], [])

     # Iterate through the available socket that needs to be read
    for userSocket in userRead:

        # A Response received from server
        if userSocket is clientConnection:
            # Get message from server
            msg = userSocket.recv(bufferSize)

            # If the server is down
            if not msg:  
                #Print error and exit script         
                print("Server is down! Sorry for your inconvinience!!!")
                sys.exit(2)

            # else the server is working, print then wait for user to add command
            else:
                # Client leaves Lobby on server
                if msg == QUITCOMMAND.encode():
                    sys.stdout.write('You have left the lobby, good bye.\n')
                    sys.exit(2)
                else:
                    # Decode message from server 
                    sys.stdout.write(msg.decode())

                    # If the user is new, add the name command
                    if 'Enter your screen name:' in msg.decode():
                        # add messge
                        msgPrefix = 'name: '

                    # Prompt the usre for a command
                    else:
                        msgPrefix = '> '
                        print('>', end=' ', flush = True)

        # User sends commands and messages to server
        else:
            # Get user input
            msg = msgPrefix + sys.stdin.readline()
            # Send message to server
            clientConnection.sendall(msg.encode())
