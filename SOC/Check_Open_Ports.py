import socket

def scan_ports(ip, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} open on {ip}")

ip_addresses = ['192.168.1.10', '192.168.1.11']
port_range = (20, 1024)

for ip in ip_addresses:
    scan_ports(ip, port_range)
