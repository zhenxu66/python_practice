import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 25800

BUFFER_SIZE = 1024
for i in range(100):Monday
    # print(i)
    if i % 4 == 0:
        message = str.encode("MEAS:a")
    else:
        message = str.encode("MEAS:b")
    time.sleep(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(message)
    s.close()

