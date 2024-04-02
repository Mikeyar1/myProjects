import requests
from bs4 import BeautifulSoup

// the website of choice
url = 'https://www.desiringgod.org/articles/life-is-for-living'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Web page fetched successfully!")
else:
    print("Failed to fetch the web page. Status code:", response.status_code)
