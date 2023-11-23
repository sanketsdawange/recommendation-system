import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sample_data.csv')

# Feature engineering with a small constant added to avoid division by zero
small_constant = 1e-10  # You can adjust this value based on your data
df['like_percentage'] = df['is_liked'] / (df['is_watched'] + small_constant)
df['comment_percentage'] = df['is_commented'] / (df['is_watched'] + small_constant)
df['share_percentage'] = df['is_shared'] / (df['is_watched'] + small_constant)

# Select features for clustering
features = ['like_percentage', 'comment_percentage', 'share_percentage']

# Normalize the data
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Choose the number of clusters (you may want to tune this)
num_clusters = 5

# Apply K-Means clustering with explicit n_init value
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df[features])

# Save the DataFrame with cluster information to CSV
df.to_csv('output.csv', index=False)

# Visualize the clusters (for 2D data)
plt.scatter(df['like_percentage'], df['comment_percentage'], c=df['cluster'], cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Like Percentage')
plt.ylabel('Comment Percentage')
plt.show()

# Display the cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
print("Cluster Centers:")
print(pd.DataFrame(cluster_centers, columns=features))

# Display the data with assigned clusters
print("Data with Clusters:")
print(df[['user_id', 'content_id', 'cluster']])