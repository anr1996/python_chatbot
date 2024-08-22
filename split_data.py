import pandas as pd
# Load your CSV file
df = pd.read_csv("wiki-conciseness-dataset/concise_full.tsv", sep="\t", header=None)

# Split the data: 80% for training, 20% for validation
train_df = df.sample(frac=0.8, random_state=42) # 80% for training
val_df = df.drop(train_df.index) # 20% for validation

# Save the validation data to a new file
val_df.to_csv("wiki-conciseness-dataset/concise_full_validation.tsv", sep="\t", header=False, index=False)