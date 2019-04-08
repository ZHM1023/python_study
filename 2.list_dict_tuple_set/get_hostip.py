
import socket
hostname = socket.gethostname()
print(hostname)
hostip = socket.gethostbyname(hostname)
print(hostip)