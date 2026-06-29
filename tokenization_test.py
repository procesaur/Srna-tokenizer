from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("procesaur/Srna_test", trust_remote_code=True)

text = "Hello world, this is a test."

# Tokenize and print tokens
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

# Encode to ids and decode back to string
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)
print("Decoded:", decoded)