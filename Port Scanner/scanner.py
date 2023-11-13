#!/bin/python3

import socket
from datetime import datetime 
import sys

#define Target
if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:

    print("Invalid Arguments")
    print("Syntext: python3 scanner.py")

#adding A pretty Banner 

print("-"*50)
print("Port Scanner Written By : M.O.B. JIHAD")
print("Scanning Started on : "+target)
print("Time Started :"+str(datetime.now()))
print("-"*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))   # if port open return 0 otherwise 1 
        if result==0:
            print("Port {} is Open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program.")
    sys.exit()

except socket.gaierror:
    print("Host name couldn't Resolved ")
    sys.exit()   

except socket.error:
    print("Could not connect to the Server.")
    sys.exit()     
