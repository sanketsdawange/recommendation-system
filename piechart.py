import pandas as pd
import matplotlib.pyplot as plt

# Load the output.csv file into a DataFrame
df = pd.read_csv('output.csv')

# Count the number of users in each cluster
cluster_counts = df['cluster'].value_counts()

# Plot a pie chart
plt.pie(cluster_counts, labels=cluster_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('User Distribution in Clusters')
plt.show()
