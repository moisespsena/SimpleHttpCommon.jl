import socket
import sys

HOST = ''	# Symbolic name, meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	print 'Socket created'

	#Bind socket to local host and port
	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
	
	print 'Socket bind complete'

	#Start listening on socket
	s.listen(10)
	print 'Socket now listening'

	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	with open(sys.argv[1], "w", 0) as f:
		while 1:
			print("whiting data...")
			f.write(conn.recv(1))
finally:
	if s: s.close()
