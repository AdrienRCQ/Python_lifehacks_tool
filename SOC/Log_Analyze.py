def search_logs(log_file, keywords):
    with open(log_file, 'r') as file:
        for line in file:
            if any(keyword in line for keyword in keywords):
                print(line.strip())

log_file = '/var/log/auth.log'
keywords = ['Failed password', 'Authentication failure', 'Invalid user']

search_logs(log_file, keywords)
