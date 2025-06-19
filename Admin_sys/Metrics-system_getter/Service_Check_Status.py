import os

def check_and_restart_service(service_name):
    status = os.system(f"systemctl is-active --quiet {service_name}")
    if status != 0:
        print(f"{service_name} is not running. Restarting...")
        os.system(f"systemctl restart {service_name}")
    else:
        print(f"{service_name} is running.")

check_and_restart_service("nginx")
