from tokenization_srna import SrnaTokenizer
# from transformers import AutoTokenizer

tokenizer = SrnaTokenizer.from_pretrained("procesaur/Srna_test", trust_remote_code=True)
#tokenizer.omit_tags=True
text = "Pitao sam se 'да ли ће ме и рођени дјед и оџак надживети'?"

# Tokenize and print tokens
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

# Encode to ids and decode back to string
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)
print("Decoded:", decoded)
