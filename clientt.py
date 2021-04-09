import socket

sock = socket.socket()
sock.setblocking(1)
#address = 'localhost'
while True:
    try:
        port = int(input('Input port: '))
        address = input('Input hostname: ')
        sock.connect((address, port))
        print('Server connection')
        break
    except socket.gaierror:
        address = '192.168.68.27'
        port = 9064
        print('Incorrect data, open socket with port = ', port, ', address - ', address)
        try:
            sock.connect((address, port))
            break
        except OSError:
            port += 1
    except ConnectionRefusedError:
        print('Smth went wrong, try again')

while True:
    sent = input('Input sentence: ')
    if sent == 'exit':
        #sock.close()
        print('Disconnection')
        break

    sock.send(sent.encode())
    print('Sending data')
    data = sock.recv(1024)
    print('Receiving data')
    print(data.decode())
print('Disconnection')