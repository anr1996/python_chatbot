import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration
from train_t5_model import ConcisenessDataset # Import the ConcisenessDataset class

# Load the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# load your validation data (replace 'path_to_validation.tsv' with the actual path)
val_df = pd.read_csv("wiki-conciseness-dataset/concise_full_validation.tsv", sep="\t", header=None)


# Create the validation dataset
val_dataset = ConcisenessDataset(val_df, tokenizer)

# Function to evaluate the model on the validation set
def evaluate_model(model, tokenizer, dataset):
    model.eval()
    predictions, actuals = [], []

    for i in range(len(dataset)):
        input_ids = dataset[i]['input_ids'].unsqueeze(0)
        attention_mask = dataset[i]['attention_mask'].unsqueeze(0)

        outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask,
                                 max_new_tokens = 50)
        prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
        actual = tokenizer.decode(dataset[i]['labels'], skip_special_tokens=True)

        predictions.append(prediction)
        actuals.append(actual)

    return predictions, actuals
    
# evaluate the model
predictions, actuals = evaluate_model(model, tokenizer, val_dataset)

# Print a few examples

for i in range(5):
    print(f"Input: {val_df.iloc[i, 0]}")
    print(f"Predicted: {predictions[i]}")
    print(f"Actual: {actuals[i]}")
    print("_" * 50)
