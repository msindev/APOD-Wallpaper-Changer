# Import necessary libraries and modules

import requests
import json

# Set API Key. Replace DEMO_KEY with your key to get more rate limits
# Default request limit for DEMO_KEY : Hourly Limit: 30 requests per IP address per hour
# Daily Limit: 50 requests per IP address per day
API_KEY = 'DEMO_KEY'


QUERY_URL = r'https://api.nasa.gov/planetary/apod?api_key='+API_KEY
