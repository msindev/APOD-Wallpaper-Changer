# Import necessary libraries and modules

import requests

# Set API Key. Replace DEMO_KEY with your key to get more rate limits
# Default request limit for DEMO_KEY : Hourly Limit: 30 requests per IP address per hour
# Daily Limit: 50 requests per IP address per day
#hd parameter returns URL for HD image
query = {'api_key' : 'DEMO_KEY', 'hd' : 'True'}

#QUERY_URL is the URL to get JSON response containing URL for APOD
QUERY_URL = r'https://api.nasa.gov/planetary/apod'

#data returns the required JSON object
#Parameters passed are api key and hd
#TimeOut is 5 seconds
data = requests.get(QUERY_URL, params = query, timeout = 5)
try:
    data.raise_for_status()
except Exception as e:
    print("Error encountered: %s" % (e))
    exit(0)

downloaded_data = data.json()

image_url = downloaded_data[hdurl]

image = requests.get(image_url)
try:
    image.raise_for_status()
except Exception as e:
    print("Error encountered: %s" % (e))
    exit(0)
