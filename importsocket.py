import socket

def discover_hosts(start_ip, end_ip, port=80):
    active_hosts = []
    for ip in range(start_ip, end_ip + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Timeout de 0.5 segundos
                s.connect((f"192.168.15.{ip}", port))
                active_hosts.append(f"192.168.15.{ip}")
        except (socket.timeout, socket.error):
            continue
    return active_hosts

# Descobrir hosts ativos no intervalo de IPs
start_ip = 1
end_ip = 254
active_hosts = discover_hosts(start_ip, end_ip)

# Exibir os hosts ativos
print("Active hosts:", active_hosts)