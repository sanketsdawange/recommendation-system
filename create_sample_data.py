import csv
import random

# Specify the number of records
num_records = 1000

# Column headers
headers = ['user_id', 'content_id', 'is_watched', 'is_liked', 'is_commented', 'is_shared']

# Generate random data
data = [[
    random.randint(1, 100),  # user_id
    random.randint(1, 500),  # content_id
    random.choice([0, 1]),   # is_watched (0 or 1)
    random.choice([0, 1]),   # is_liked (0 or 1)
    random.choice([0, 1]),   # is_commented (0 or 1)
    random.choice([0, 1])    # is_shared (0 or 1)
] for _ in range(num_records)]

# Write to CSV file
with open('sample_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write headers
    csv_writer.writerow(headers)
    
    # Write data
    csv_writer.writerows(data)

print("CSV file 'sample_data.csv' created successfully.")
