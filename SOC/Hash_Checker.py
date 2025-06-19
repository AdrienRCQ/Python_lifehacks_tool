import hashlib

def check_file_hash(file_path, known_hash):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
        if file_hash == known_hash:
            print("Warning: File matches known malicious hash!")
        else:
            print("File is clean.")

file_path = '/path/to/file.exe'
known_hash = input('Enter the hash : ')
check_file_hash(file_path, known_hash)
