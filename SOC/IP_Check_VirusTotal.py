import requests

def check_ip_virustotal(ip_address, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"IP {ip_address} analysis results: {data}")
    else:
        print(f"Failed to retrieve data for IP {ip_address}")

api_key = 'YOUR_API_KEY'
iptocheck = input('Enter the IP to check : ')
check_ip_virustotal(iptocheck, api_key)
