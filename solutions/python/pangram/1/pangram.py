def is_pangram(sentence):
    allchars = set()
    
    for character in sentence.lower():
        if character.isalpha():
            allchars.add(character)

    return len(allchars)==26
