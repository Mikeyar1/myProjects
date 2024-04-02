import requests
from bs4 import BeautifulSoup
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_parse(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            logging.warning(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def extract_article_details(soup):
    articles = soup.find_all('article')
    data = []
    for article in articles:
        
        # Needs to be initialized
        article_data = {
            'title': None,
            'publication_date': None,
            'author': None,
            'snippet': None,
            'url': None
        }

=        try:
            article_data['title'] = article.find('h2').get_text(strip=True)
            article_data['publication_date'] = article.find('time').get_text(strip=True)
            article_data['author'] = article.find('p', class_='author').get_text(strip=True) if article.find('p', class_='author') else 'No author'
            article_data['snippet'] = article.find('p', class_='snippet').get_text(strip=True)[:100] + '...' if article.find('p', class_='snippet') else 'No snippet'
            article_data['url'] = article.find('a')['href'] if article.find('a') else 'No URL'

            data.append(article_data)
        except Exception as e:
            logging.error(f"Error extracting article details: {e}")
    
    return data

#  URL
url = 'https://www.desiringgod.org/articles/life-is-for-living'
soup = fetch_and_parse(url)
if soup:
    data = extract_article_details(soup)
    if data:
        logging.info("Data extracted successfully!")
        for article in data:
            print(article)
    else:
        logging.warning("No articles found.")
else:
    logging.error("Failed to parse the webpage.")
