# Import necessary libraries and modules

import requests
from PIL import Image
from io import BytesIO
import os
import platform
import ctypes
import time

def directory():
    if platform.system() == "Windows":
        dir_to_save = 'C:\\APOD\\'
    elif platform.system() == "Linux":
        dir_to_save = '~/APOD/'
    return dir_to_save

def getImage():
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
    image_path = ""

    if not os.path.exists(directory()):
        os.makedirs(directory)

    if not image_name in os.listdir(directory()):
        image = requests.get(image_url)
        try:
            image.raise_for_status()
        except Exception as e:
            print("Error encountered: %s" % (e))
            exit(0)

        img = Image.open(BytesIO(image.content))

        image_path = os.path.join(directory(), image_name)
        img.save(image_path)
    else:
        image_path = os.path.join(directory(), image_name)
    return image_path

def setWallpaper(image_path):
    if platform.system() == "Windows":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)
    elif platform.system() == "Linux":
        command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '%s'" % image_path
        status, output = commands.getstatusoutput(command)

def main():
    while(True):
        image_path = getImage()
        setWallpaper(image_path)
        time.sleep(3600)
if __name__ == "__main__":
    main()
