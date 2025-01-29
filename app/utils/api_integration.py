"""
Author: Ashwin Nair
Date: 2025-01-28
Project name: api_integration.py
Summary: Enter summary here.
"""

import requests

def check_ip_reputation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}
