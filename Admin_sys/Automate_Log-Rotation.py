import os
import shutil
import time

def rotate_logs(log_dir, days):
    now = time.time()
    cutoff = now - (days * 86400)

    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if os.path.isfile(file_path):
            file_time = os.path.getmtime(file_path)
            if file_time < cutoff:
                shutil.make_archive(file_path, 'zip', log_dir, filename)
                os.remove(file_path)
                print(f"Archived and removed {filename}")

rotate_logs('/var/log/myapp', 7)
