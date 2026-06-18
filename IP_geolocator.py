#!/usr/bin/env python3
"""
IP Geolocation Lookup Tool
"""

import requests
import sys
import json

# Free IP geolocation API (no API key required)
# Rate limited to ~50 requests per minute
API_URL = "http://ip-api.com/json/"

def get_public_ip():
    """Get your current public IP address."""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json()["ip"]
    except requests.exceptions.RequestException as e:
        print(f" Error fetching public IP: {e}")
        return None
