# Import the required python components
import socket,User

# Create the Room class that holds all the chat rooms
class Room:

    # Create constructor
    def __init__(self, name):
        # Hold messages history
        self.msgHistory = ''
        # The list of sockets for the room
        self.users = []
        # Hold room name
        self.name = name  

    # Welcome the user
    def welcomeNewUser(self, currentUser):
        # Generate welcoming message
        welcomeMsg = currentUser.name + ", welcome to : " + self.name + '\n'

        # Sends the history to only the new user
        self.msgHistory = self.msgHistory + welcomeMsg
        currentUser.socket.sendall(self.msgHistory.encode())

        # Send welcome message to every user 
        for user in self.users:
            if user.name != currentUser.name:
                user.socket.sendall(welcomeMsg.encode())

    # Boadcast message to other users
    def broadcast(self, currentUser, msg):
        # Generates the message and add name others know
        msg = currentUser.name + msg

        # Update the message History
        self.msgHistory = self.msgHistory + str(msg)

        # Send the msg to all the user in the chat room
        for user in self.users:
            user.socket.sendall(msg.encode())

    # Remove a user from a room
    def removeUser(self, user):

        #Remove the user from the users list
        self.users.remove(user)

        #broadcast the message that the user has left the room
        msg = " has left the room\n"
        self.broadcast(user, msg)