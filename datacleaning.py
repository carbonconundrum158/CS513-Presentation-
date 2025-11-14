import pandas as pd
import requests
import os

# Download files if they don't exist
urls = {
    'Outcomes-a.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-a.txt',
    'Outcomes-b.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-b.txt'
}

for filename, url in urls.items():
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(requests.get(url).content)

# Read and combine files
outcomes_a = pd.read_csv('Outcomes-a.txt')
outcomes_b = pd.read_csv('Outcomes-b.txt')
df = pd.concat([outcomes_a, outcomes_b], ignore_index=True)

print("Combined shape:", df.shape)
print("Missing per column:\n", df.isnull().sum())
