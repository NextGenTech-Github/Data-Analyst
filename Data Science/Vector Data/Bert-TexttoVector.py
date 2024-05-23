# pip install transformers torch

from transformers import BertModel, BertTokenizer
import torch

# Load pre-trained BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def generate_text_vector(text):
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    # Get the mean of the output hidden states to form the vector
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

text = "Example text for vectorization."
text_vector = generate_text_vector(text)
print(text_vector)
