import threading
import socket

print('Server start')
sock = socket.socket()
port = 9064

while True:
    try:
        sock.bind(('', port))
        print('Port connected', port)
        break
    except OSError:
        port += 1

sock.listen(0)
sent = ''


def data_srv(conn, addr):
	sent = ''
	print('Client connection')
	print('connected:', addr)
	while True:
		print('Receiving data')
		data = conn.recv(1024)
		print(data)
		if not data:
			break
		sent += data.decode()
		print('Sending data')
		conn.send(data)
	print(sent)
	conn.close()

while True:
	conn, addr = sock.accept()
	th = threading.Thread(target=data_srv, args=(conn, addr))
	th.start()