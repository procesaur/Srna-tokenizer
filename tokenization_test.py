from tokenization_srna import SrnaTokenizer
# from transformers import AutoTokenizer

tokenizer = SrnaTokenizer.from_pretrained("procesaur/Srna_test", trust_remote_code=True)
#tokenizer.omit_tags=True
text = "Pitao sam se 'да ли ће ме и рођени дјед и оџак надживети'?"
# text = "This is a test 😊\nI was born in 92000, and this is falsé.\n生活的真谛是\nHi  Hello\nHi   Hello\n\n \n  \n Hello\n<s>\nhi<s>there\nThe following string should be properly encoded: Hello.\nBut ird and ปี   ird   ด\nHey how are you doing"
# Tokenize and print tokens
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

# Encode to ids and decode back to string
ids = tokenizer.encode(text)
print(ids)
decoded = tokenizer.decode(ids)
print("Decoded:", decoded)
