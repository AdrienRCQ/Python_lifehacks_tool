import shutil
import smtplib
from email.mime.text import MIMEText

def check_disk_usage(disk, threshold):
    total, used, free = shutil.disk_usage(disk)
    usage_percent = (used / total) * 100
    return usage_percent > threshold

def send_alert_email(cpu_usage):
    msg = MIMEText(f"Attention: Disk usage is at {cpu_usage}%")
    msg['Subject'] = 'High Disk Usage Alert'
    msg['From'] = 'alerte@example.com'
    msg['To'] = 'recipient@example.com'
    smtp_password = input('Enter your SMTP password : ')

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('alerte@example.com', smtp_password)
        server.send_message(msg)


if check_disk_usage("/", 80):
    send_alert_email()
