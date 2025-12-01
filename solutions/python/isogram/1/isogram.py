def is_isogram(string):
    
    set_characters = set()
    
    for character in string.lower():
        if character.isalpha():
            if character in set_characters:
                return False
            set_characters.add(character)

    return True
            
