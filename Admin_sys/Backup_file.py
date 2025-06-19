import shutil
import os
from datetime import datetime

def backup_config_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f"config_backup_{timestamp}")
    shutil.copytree(source_dir, backup_path)
    print(f"Backup completed successfully at {backup_path}")

source_dir = '/etc/myapp'
backup_dir = '/backup/configs'
backup_config_files(source_dir, backup_dir)
