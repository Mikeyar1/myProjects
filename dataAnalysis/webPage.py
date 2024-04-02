import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of URLs to scrape
urls = [
    'https://www.desiringgod.org/articles/life-is-for-living'
]

articles = []

def fetch_article_details(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title, publication date, and content with more flexible selectors
            title = soup.find('h1').get_text(strip=True)
            date = soup.find('time', {'class': 'published'})['datetime'] if soup.find('time', {'class': 'published'}) else 'No date found'
            content = ' '.join([p.get_text(strip=True) for p in soup.find('article').find_all('p')]) if soup.find('article') else 'No content found'

            return {
                'title': title,
                'publication_date': date,
                'content': content[:100] + '...'  # Truncate content for demonstration
            }
        else:
            logging.warning(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

for url in urls:
    article = fetch_article_details(url)
    if article:
        articles.append(article)
    time.sleep(1)  # Rate limiting

# Convert to pandas DataFrame
df = pd.DataFrame(articles)

# Save to CSV
df.to_csv('articles.csv', index=False)

logging.info("Scraping completed. Data saved to articles.csv.")
print(df)

