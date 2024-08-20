from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')


# Example input and target text (replace with your actual data)
input_text = "Your input sentence here."
target_text = "Your concise sentence here."

# Tokenize the input and target text
input_ids = tokenizer(input_text, return_tensors="pt").input_ids
target_ids = tokenizer(target_text, return_tensors="pt").input_ids

# Print out the tokenized IDs to verify
print("Input IDs:", input_ids)
print("Target IDs:", target_ids)

