import re

def detect_suspicious_commands(history_file):
    suspicious_patterns = ['nmap', 'nc ', 'netcat', 'rm -rf', 'curl ', 'wget ']
    with open(history_file, 'r') as file:
        for line in file:
            if any(re.search(pattern, line) for pattern in suspicious_patterns):
                print(f"Suspicious command found: {line.strip()}")

history_file = '/home/user/.bash_history'
detect_suspicious_commands(history_file)
