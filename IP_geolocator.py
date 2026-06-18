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


def lookup_ip(ip_address):
    """
    Look up geolocation data for a given IP address.
    Returns a dictionary with location information.
    """
    try:
        # Make the API request with a timeout
        response = requests.get(f"{API_URL}{ip_address}", timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if the API returned a successful response
        if data.get("status") == "success":
            return data
        else:
            print(f" API Error: {data.get('message', 'Unknown error')}")
            return None
            
    except requests.exceptions.Timeout:
        print(" Request timed out. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        print(" Network error. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f" An error occurred: {e}")
        return None

