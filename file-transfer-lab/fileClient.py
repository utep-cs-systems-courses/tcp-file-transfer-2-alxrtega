#!/usr/bin/env python3
import socket, sys, re
sys.path.append("../lib")       # for params
import params

'''
@author Alex Ortega

this file contains the client's portion of simple client-server file 
transfer. the client and the server must establish a connection through
sockets and ports
'''

class Client:

    switchesVarDefaults = None
    programName         = None
    paramMap            = None
    server              = None
    usage               = None
    debug               = None
    addressFamily       = None
    socketType          = None
    addressPort         = None
    clientSocket        = None
    filename            = None

    def __init__(self):
        self.switchesVarDefaults = (
            (('-s', '--server'), 'server', "127.0.0.1:50001"),
            (('-d', '--debug'), "debug", False), # boolean (set if present)
            (('-?', '--usage'), "usage", False), # boolean (set if present)
            )

        paramMap = params.parseParams(self.switchesVarDefaults)

        self.server, self.usage, self.debug = paramMap["server"], paramMap["usage"], paramMap["debug"]

        if self.usage:
            params.usage()

        try:
            serverHost, serverPort = re.split(":", self.server)
            serverPort = int(serverPort)
        except:
            print("Can't parse server:port from '%s'" % self.server)
            sys.exit(1)

        self.addressFamily = socket.AF_INET
        self.socketType    = socket.SOCK_STREAM
        self.addressPort   = (serverHost, serverPort)

        self.clientSocket = socket.socket(self.addressFamily, self.socketType)
        if self.clientSocket is None:
            print('could not open socket')
            sys.exit(1)
        print("Waiting to be connected...")
        self.clientSocket.connect(self.addressPort)
        print("Connected...")

        self.filename = input(str("Enter a file name: "))
        with open(self.filename, "r") as sending:
            fileData = sending.read(1024)
            data = self.clientSocket.send(str(fileData).encode('utf-8'))
        print("The file has been transferred.")
        self.clientSocket.close()

client = Client()