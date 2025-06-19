import collections

def detect_port_scans(log_file):
    ip_attempts = collections.defaultdict(int)
    with open(log_file, 'r') as file:
        for line in file:
            if "Connection attempt" in line:
                ip = line.split()[1]  # Supposons que l'IP soit en deuxième position
                ip_attempts[ip] += 1

    for ip, attempts in ip_attempts.items():
        if attempts > 100:  # Par exemple, plus de 100 tentatives de connexion
            print(f"Potential port scan detected from {ip} with {attempts} attempts")

log_file = '/var/log/connection.log'
detect_port_scans(log_file)
