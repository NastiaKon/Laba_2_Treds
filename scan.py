import threading
import socket
from time import sleep
from progress.bar import Bar

#  address = '192.168.68.27'
address = '192.168.68.27'
ports=[]

def check_ports(bar, l, r):
    global ports
    for port in range(l, r):
        bar.next()
        sock = socket.socket()
        try:
            sock.connect((address, port))
            ports.append(port)
            sock.close()
        except ConnectionRefusedError:
            pass
        except OSError:
            pass
        except TimeoutError:
            pass

threads=[]
bar = Bar('Processing', max=65536)

#512 potokov
for i in range(1, 513):
    th = threading.Thread(target=check_ports, args=(bar, (i-1)*128, i*128))
    threads.append(th)
    th.start()
for th in threads:
    th.join()


print('\nPorts:')
ports.sort()
bar.finish()
for i in ports:
    print(i)