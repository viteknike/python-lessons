import socket

SERVER_ADDRESS = ('localhost', 15253)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes('5', 'utf-8'))
data = client.recv(4096)
print(data.decode('utf-8'))

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes('10', 'utf-8'))
data = client.recv(4096)
print(data.decode('utf-8'))

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes('eXit', 'utf-8'))
data = client.recv(4096)
client.close()
