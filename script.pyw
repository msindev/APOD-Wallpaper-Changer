# Import necessary libraries and modules

import requests
from PIL import Image
from io import BytesIO
import os

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

image_url = downloaded_data['url']
image_name = image_url[image_url.rindex('/') + 1 : ]

image = requests.get(image_url)
try:
    image.raise_for_status()
except Exception as e:
    print("Error encountered: %s" % (e))
    exit(0)

img = Image.open(BytesIO(image.content))

dir_to_save = 'C:\\APOD\\'
if not os.path.exists(dir_to_save):
    os.makedirs(dir_to_save)

img.save(os.path.join(dir_to_save, image_name))
