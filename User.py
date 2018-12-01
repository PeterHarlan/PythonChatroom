# Import the required python components
import socket

#Define the user class
class User:
	# Create constructor
    def __init__(self, socket, name = "Username"):
    	# Set blocking to false
    	socket.setblocking(0)
    	self.socket = socket
    	self.name = name

    # Needed for select.select to returns file descripter, -1 on error
    def fileno(self):
        return self.socket.fileno()
