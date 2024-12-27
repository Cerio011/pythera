import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('www.hackthissite.org', 80)  # Substitua pelo domínio correto
client_socket.connect(server_address)

# Send data
message = 'GET / HTTP/1.0\r\nHost: www.hackthissite.org\r\n\r\n'  # Adicionando o cabeçalho Host
client_socket.sendall(message.encode())

# Receive the response
response = b""  # Inicialize a resposta como bytes
while True:
    part = client_socket.recv(4096)
    if not part:
        break  # Sai do loop quando não houver mais dados
    response += part

print(response.decode())

# Close the connection
client_socket.close()