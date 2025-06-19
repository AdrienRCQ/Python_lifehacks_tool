import psutil
import datetime as datetime
import pandas as pd
import os
import time

def metrics_getter():
    csv_file = 'process_monitoring.csv'
    is_it_exist(csv_file)
    df = pd.read_csv(csv_file, sep=";")
    actual = datetime.datetime.now()

    cpu_percent_use = psutil.cpu_percent()
    disk_percent_use = psutil.disk_usage("C:\\").percent
    ram_percent_use = psutil.virtual_memory().percent

    show = pd.DataFrame([[
        actual.strftime("%d-%m-%Y %X"),
        actual.strftime("%d-%m-%Y"),
        actual.strftime("%X"),
        cpu_percent_use,
        f"{disk_percent_use}%",
        f"{ram_percent_use}%"]]
        ,columns = ["datetime", "date", "time", "CPU Usage", "Disk Usage", "RAM Usage"])

    # df = pd.DataFrame()
    # df1 = df.join(show)
    df = df._append(show)
    df.to_csv(csv_file, sep=";", index=False)
    print (cpu_percent_use, disk_percent_use, ram_percent_use)



def is_it_exist(this_path):
    if os.path.exists(this_path):
        print('file already exists')
    else:
        # create a file
        with open(this_path, 'w') as fp:
            # uncomment if you want empty file
            fp.write('This is first line')
            print("ok")

def cpu_alerte():
    # Optional: give the system time to stabilize CPU stats
    time.sleep(1)

    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

    if cpu_percent >= 80:
        print("⚠️ High CPU usage detected!")
    else:
        print("✅ CPU usage is normal.")

if __name__ == "__main__":
    metrics_getter()