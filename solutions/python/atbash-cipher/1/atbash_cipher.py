import re

def encode(plain_text):

    # Define the translation table
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz1234567890", "zyxwvutsrqponmlkjihgfedcba1234567890")
    cleaned = re.sub(r'[^A-Za-z0-9]', '', plain_text).lower()
    
    # Apply the translation to a string
    return " ".join(cleaned.translate(table)[i:i+5] for i in range(0, len(cleaned), 5))


def decode(ciphered_text):
    return encode(ciphered_text).replace(" ","")
