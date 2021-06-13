#!usr/bin/env python

from pexpect import pxssh
import getpass
import socket
import sys

## CLIENT-SERVER INTERACTION THRU SOCKET ##
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:

	hostname = '192.168.56.103'
	portnumber = 8004

	soc.connect((hostname,portnumber))

	info = soc.recv(1024)
	soc.send(b'***************** Hello From Client!!! ********************')
	print(info.decode('utf-8'))

## SSH PROTOCOL , CLIENT -> SERVER(REMOTE), ##
try:
   client = pxssh.pxssh()
   raw_input = input
   host_server = raw_input('SERVER_HOSTNAME: ')
   username_server = raw_input ('SERVER_USERNAME: ')
   password_server = getpass.getpass('SERVER_PASSWORD: ')
   client.logfile =sys.stdout.buffer
   client.login (host_server, username_server, password_server)
   client.sendline ('hostname')
   client.prompt()
   print (client.before.decode('utf-8'))
   client.sendline('ls -l')
   client.prompt()
   print (client.before.decode('utf-8'))
   client.sendline ('hostname -I')
   client.prompt()
   print (client.before.decode('utf-8'))
   client.logout()
except pxssh.ExceptionPxssh as e:
   print ("\n ********************* THANKS FOR CONNECTING *******************\n")
   print ('',str(e))
