#!/usr/bin/env python

from pexpect import pxssh
import getpass
import sys
import socket
import time

## INTERACTION CLIENT-SERVER THRU SOCKET ##
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
	hostname = socket.gethostname()
	hostnameIP = socket.gethostbyname(hostname)
	portnumber = 8004

	soc.bind(('',portnumber))
	print("Server binded to " + str(portnumber))

	soc.listen(5)
	print("Waiting for connection...")

	con, addr = soc.accept()
	print ("Connected to " + str(addr))
	con.send(b'*********************** Hi from Server!!! ********************************')
	info =con.recv(1024)
	print(info.decode('utf-8'))


## SSH CONNECTION FROM SERVER TO SERVER (HOSTNAME) FOR DEBUG PURPOSE ##
try:
	server = pxssh.pxssh()
	raw_input = input
	my_hostname = raw_input('HOSTNAME: ')
	my_username = raw_input('USERNAME: ')
	my_password = getpass.getpass('PASSWORD: ')
	if not server.login ('my_hostname', 'my_username', 'my_password'):
		print ('SSH SESSION IS HAVING SOME FAILURE, BE PATIENT AND TRY AGAIN\n', str(server))
	else:
		print ("SSH SESSION LOGIN SUCESSFUL, GOOD JOB !!!!!")
		server.sendline('hostname')
		server.prompt()
		print (server.before)
		server.logout()


	server.sendline('uptime;df -h')

except pxssh.ExceptionPxssh:
	print("******************* THANKS FOR CONNECTING ****************")
