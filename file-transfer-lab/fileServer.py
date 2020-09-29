#!/usr/bin/env python3
import socket, sys, re
sys.path.append("../lib")       # for params
import params

'''
@author Alex Ortega

this file contains the server's portion of simple client-server file 
transfer. the client and the server must establish a connection through
sockets and ports
'''

class Server:

    switchesVarDefaults = None
    progname            = None
    debug               = None
    listenPort          = None
    serverSocket        = None
    connection          = None
    address             = None

    def __init__(self):
        self.switchesVarDefaults = (
            (('-l', '--listenPort') ,'listenPort', 50001),
            (('-d', '--debug'), "debug", False), # boolean (set if present)
            (('-?', '--usage'), "usage", False), # boolean (set if present)
            )

        self.progname = "echoserver"
        paramMap = params.parseParams(self.switchesVarDefaults)

        self.debug, self.listenPort = paramMap['debug'], paramMap['listenPort']
        self.listenAddr = ''       # Symbolic name meaning all available interfaces

        if paramMap['usage']:
            params.usage()
        
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bindAddr = ("127.0.0.1", self.listenPort)
        serverSocket.bind(bindAddr)
        serverSocket.listen(1)              # allow only one outstanding request
        # serverSocket is a factory for connected sockets

        print("Waiting to be connected...")
        self.connection, self.address = self.serverSocket.accept()  # wait until incoming connection request (and accept it)
        print('Connected by', self.address)

        #from framedSock import framedSend, framedReceive
        filename = input(str("Please enter the name of the file that will save data: "))
        with open(filename, "w") as writing:
            fileData = self.connection.recv(1024)
            utfData = fileData.decode('utf-8')
            for line in utfData:
                writing.write(line)

        print("Data has been sent successfully!")
        writing.close()

        self.connection.close()

server = Server()