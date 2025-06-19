import os

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_minutes = uptime_seconds / 60
            print(f"System uptime: {uptime_minutes:.2f} minutes")
    except Exception as e:
        print(f"Failed to read uptime: {e}")

get_uptime()
