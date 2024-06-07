import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv(".env")

# Get environment variables
zone_id = os.getenv('ZONE_ID')
auth_email = os.getenv('AUTH_EMAIL')
auth_key = os.getenv('AUTH_KEY')

def list_dns_records(zone_id, auth_email, auth_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "X-Auth-Email": auth_email,
        "X-Auth-Key": auth_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# List DNS records and print their IDs
dns_records = list_dns_records(zone_id, auth_email, auth_key)
for record in dns_records['result']:
    print(f"Record Name: {record['name']}, Record ID: {record['id']}, Record Type: {record['type']}")