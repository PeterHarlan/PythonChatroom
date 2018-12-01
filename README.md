# Chatroom project
## Introduction
This project is a chat room built with Python and socket programming. 

When the chatClient.py first becomes connected to the chatServer.py, the user lands in the Lobby. The user then inputs a name that will be displayed during the lifetime of the chatServer. Once in the lobby, the chatClient can create a chatroom, join an existing room, switch between rooms, leave the room, and exit the lobby (terminate the session).

Below are the command of the chatServer:

[commands] used to display all the possible commands
[create RoomName] used to create a room
[list] used to lists all available rooms
[join RoomName] used for joining and switching rooms
[leave] used to leave a room but stay in the lobby
[quit] used to terminate the session (leave the lobby)

If there are no chatrooms, the user must create a chatroom before communicating with other people or they must wait for another user to create a chat room and use the join command to enter that room. The user can use the list command to constantly refresh the available rooms and the number of users in the room. If the user wish to join another room but alread in a room, (s)he can use the [join RoomName] command (Replacing RoomName with the actual room name, the brackets are not typed into the cmd). 

A special feature of this chatroom project is that everything a user types into a chatroom is recorded in to a history log. The history log is sent to every new user of the chatroom.

## Installation:

1. To setup the server, open the project location in command prompt and type: "python3 chatServer.py [Server IP Address]". Note: There can be at most 10 clients connected to the server at a given time. This can be altered to in the chatServer.py file by altering the value of MAXCLIENTS. 

    The following output message on the server indicates that the server is running:
    "Hosting at " + ServerIPAddress

2. To setup the client to communicate with the server, type "python3 chatClient.py [Server IP Address]" into the cmd. 

    The following output message on the client indicates that the client is running:
    
    "Connected to server"

3. The user at the client host is encouraged to enter a name into the client's terminal (e.g. "Joe", "Peter", etc). If the user does not enter a name, a name will be generate using the syntax "Guest" + userCount. After the name selection process is finished, the client will be provided with a list of possible command that the server can run (As described above)

## Methodology
Objects are used to help organize this project. For instance, the objects are: Lobby, Room, and User. Only the chatServer.py uses the Lobby object. 

A TCP stream is used to handle the communication instead of UDP as established with the socket(socket.AF_INET, socket.SOCK_STREAM) command. Traditional thread module are not used in this project but instead the select module is used. The .select(rlist, wlist, xlist[, timeout]) API is used to identify if the input or output channel is ready. This API is used in both the client and server script to allow for multiple connection channels. In addition the setblocking(0) command is required to allow for multiple device connections.  

Everytime a client connects to the server, the connection is stored into the connectionList variable to keep track of all the connections which supports multiple users. 

Only the basic network functionalities exists in the chatServer.py file to keep the code simple. The processing of the user's input and comments are done through the Lobby object. Although recev() is in the chatServer.py file, the sendall() command is called through the Lobby object (the sendall() repeatly calls send() within itself to hand large data that needs to be transmitted). 

## Summary of Achievements
The project allows multiple user to communicate with each other after joining a lobby. All the described commands in the introduction are implemented. An internal history feature is also implemented (external history logs are not created). 

## Potential Problems
Since no containers were used in this project, the server cannot scale quickly. In addition, if the server were to crash, recovery is impossible since the server does not record the log of the users on the server, chatrooms and history messages to an external file. Moreover, there is no max limit on the number of line of history that will be sent to the client. Let say there are 1 million lines of previous chat history, a new user will be sent all 1 million lines of data. This can lead to side effects associated with a DoS attack for both the client and the server. For instance, the server may be powerful enough to send 1 million lines of data but the client cannot handle the signifigant stream of data that is transmitted. On the other hand, if many hosts decides to join a chatroom with a signifigant chat history, this can eat up all the resources on the server trying to transmit the large chat history.

## Source
This source describes the basic implementations of server and client scripts in python to allow for multiple users. 
https://steelkiwi.com/blog/working-tcp-sockets/