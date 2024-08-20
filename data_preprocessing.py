import pandas as pd

# Load the dataset (replace 'path_to_your_dataset.csv' with the actual path)
df = pd.read_csv('/Users/adrianrich/Documents/python/chatbot_project/Grid view.csv')

# Display the first few rows
print(df.head())

# Get some basic info about the dataset
print(df.info())

