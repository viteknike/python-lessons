import socket

SERVER_ADDRESS = ('', 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print('Ждем подключения клиента...')
while True:
    c, a = server.accept()
    data = c.recv(4096)
    print('Получили от клиента:', data.decode('utf-8'))
    if data.decode('utf-8').lower() == 'exit':
        break
    else:
        data = str(int(data.decode('utf-8'))*10)
        c.send(bytes(f'{data}', 'utf-8'))
        c.close()
