soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

# Extract titles and publication dates
data = []
for article in articles:
    title = article.find('h2').text  
    date = article.find('time').text  
    data.append({'title': title, 'publication_date': date})

print("Data extracted successfully!")
