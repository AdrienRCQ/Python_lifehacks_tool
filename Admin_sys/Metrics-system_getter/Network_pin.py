import os

def ping_host(host):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is up")
    else:
        print(f"{host} is down")

hosts = ["192.168.1.1", "google.com", "192.168.1.2"]

for host in hosts:
    ping_host(host)
