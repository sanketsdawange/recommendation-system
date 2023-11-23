import csv
import random

num_records = 1000

headers = ['user_id', 'content_id', 'is_watched', 'is_liked', 'is_commented', 'is_shared']

data = [[
    random.randint(1, 100),  
    random.randint(1, 500),  
    random.choice([0, 1]),   
    random.choice([0, 1]),   
    random.choice([0, 1]),   
    random.choice([0, 1])
] for _ in range(num_records)]

with open('sample_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(headers)
    
    csv_writer.writerows(data)
