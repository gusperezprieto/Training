def rotate(text, key):
    letters_small = "abcdefghijklmnopqrstuvwxyz"
    letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphered = ""

    key %= 26

    for character in text:
        if not character.isalpha():
            ciphered += character
        elif character.islower():
            ciphered += letters_small[(letters_small.find(character) + key) % 26]
        else:
            ciphered += letters_big[(letters_big.find(character) + key) % 26]

    return ciphered
