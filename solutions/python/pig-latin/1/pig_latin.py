def translate(text):

    def first_vowel_index(s):
        vowels = "aeiouAEIOU"
        indices = [i for i, char in enumerate(s) if char in vowels]
        return indices[0] if indices else -1

    def transalte_word(word):

        index_vowel = first_vowel_index(word)
        index_qu = word.find("qu")
        index_y = word.find("y")
        
        if word.startswith("xr") or word.startswith("yt") or index_vowel == 0:
            return word + "ay"
    
        if index_qu >= 0 and (index_vowel < 0 or index_qu < index_vowel):
            return word[index_qu + 2:] + word[:index_qu+2] + "ay"
    
        if index_vowel >=1:
            return word[index_vowel:] + word[:index_vowel] + "ay"
    
        if index_y >= 0 and (index_vowel < 0 or index_y < index_vowel):
            return word[index_y:] + word[:index_y] + "ay"
    
        return word


    words = text.split()

    for index, value in enumerate(words):
        words[index] = transalte_word(value)

    return " ".join(words)
