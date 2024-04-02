import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Convert the index to datetime to ensure proper plotting
publication_frequency.index = pd.to_datetime(publication_frequency.index)

# Time Series Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=publication_frequency)
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.title('Article Publication Frequency Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

]
frequency_pivot = publication_frequency.reset_index()
frequency_pivot['day'] = frequency_pivot['index'].dt.day
frequency_pivot['month'] = frequency_pivot['index'].dt.month
frequency_pivot = frequency_pivot.pivot("day", "month", "publication_date")

plt.figure(figsize=(12, 9))
sns.heatmap(frequency_pivot, cmap="YlGnBu", annot=True, fmt="d")
plt.title('Heatmap of Publication Frequency by Day and Month')
plt.xlabel('Month')
plt.ylabel('Day')
plt.show()

