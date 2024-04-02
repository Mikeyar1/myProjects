]import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data is already populated from the web scraping.
df = pd.DataFrame(data)

## Convert publication dates to datetime                                                                      
df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
df.dropna(subset=['publication_date'], inplace=True)  # Drop rows where conversion failed

## to fill
df.fillna({'title': 'Unknown', 'author': 'Unknown', 'snippet': 'Unknown'}, inplace=True)

## Publication Frequency by Date
publication_frequency = df['publication_date'].dt.date.value_counts().sort_index()

## Author Productivity
author_productivity = df['author'].value_counts()

## Analyzing Article Length (using snippet length as a proxy)
df['snippet_length'] = df['snippet'].apply(len)

# Visualization
plt.figure(figsize=(12, 6))
publication_frequency.plot(kind='line')
plt.title('Publication Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('publication_frequency.png')
plt.show()

## Author Productivity
plt.figure(figsize=(10, 8))
sns.barplot(x=author_productivity.values, y=author_productivity.index)
plt.title('Author Productivity')
plt.xlabel('Number of Articles')
plt.ylabel('Author')
plt.tight_layout()
plt.savefig('author_productivity.png')
plt.show()

## Snippet Length Distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['snippet_length'], bins=30, kde=True)
plt.title('Distribution of Article Snippet Lengths')
plt.xlabel('Snippet Length')
plt.ylabel('Frequency')
plt.savefig('snippet_length_distribution.png')
plt.show()

# Export Analyzed Data to CSV
df.to_csv('theAnalyzedData.csv', index=False)

print("Data analysis completed and results exported into an csv file.")
