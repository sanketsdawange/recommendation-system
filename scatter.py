import pandas as pd
import matplotlib.pyplot as plt

# Load the output.csv file into a DataFrame
df = pd.read_csv('output.csv')

# Scatter plot of clusters
plt.scatter(df['like_percentage'], df['comment_percentage'], c=df['cluster'], cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Like Percentage')
plt.ylabel('Comment Percentage')
plt.show()
