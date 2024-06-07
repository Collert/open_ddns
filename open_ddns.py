import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(".env")

# Get environment variables
zone_id = os.getenv('ZONE_ID')
record_id = os.getenv('RECORD_ID')
auth_email = os.getenv('AUTH_EMAIL')
auth_key = os.getenv('AUTH_KEY')
domain = os.getenv('RECORD_NAME')

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text.strip()

def update_dns_record(zone_id, record_id, auth_email, auth_key, ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "X-Auth-Email": auth_email,
        "X-Auth-Key": auth_key,
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": domain,
        "content": ip,
        "ttl": 120,
        "proxied": True
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

ip = get_public_ip()
print(update_dns_record(zone_id, record_id, auth_email, auth_key, ip))