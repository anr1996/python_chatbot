import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# Load the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Load the T5 Dataset class for your data
class ConcisenessDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_len=512):
        self.tokenizer = tokenizer
        self.data = dataframe
        self.max_len = max_len

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        source_text = str(self.data.iloc[index, 0])
        target_text = str(self.data.iloc[index, 1])

        source = self.tokenizer.encode_plus(
            source_text,
            max_length=self.max_len,
            padding='max_length',
            truncation = True,
            return_tensors="pt"
        )

        target = self.tokenizer.encode_plus(
            source_text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors="pt"
        )

        source_ids = source['input_ids'].squeeze()
        source_mask = source['attention_mask'].squeeze()

        target_ids = target['input_ids'].squeeze()
        target_mask = target['attention_mask'].squeeze()

        return {
            'input_ids' : source_ids,
            'attention_mask' : source_mask,
            'labels' : target_ids
        }

# Load your CSV file
df = pd.read_csv("wiki-conciseness-dataset/concise_full.tsv", sep="\t", header=None)

# Create the dataset
dataset = ConcisenessDataset(df, tokenizer)

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=5,
    per_device_train_batch_size=8,
    learning_rate=3e-5,
    warmup_steps=1000,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    save_total_limit=2,
    save_steps=1000,
)

# Create a Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Start training
trainer.train()




