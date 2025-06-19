''' 
Vérification de la charge CPU sur une machine + envoie d'un mail dans le cas où la limite est atteinte.
'''

import psutil
import smtplib
from email.mime.text import MIMEText

def monitor_server_load(threshold):
    load_average = psutil.getloadavg()[0]  # Charge moyenne sur 1 minute
    if load_average > threshold:
        send_alert_email(load_average)
        
def send_alert_email(cpu_usage):
    msg = MIMEText(f"Attention: CPU usage is at {cpu_usage}%")
    msg['Subject'] = 'High CPU Usage Alert'
    msg['From'] = 'alerte@example.com'
    msg['To'] = 'recipient@example.com'
    smtp_password = input('Enter your SMTP password : ')

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('alerte@example.com', smtp_password)
        server.send_message(msg)

monitor_cpu(80)
