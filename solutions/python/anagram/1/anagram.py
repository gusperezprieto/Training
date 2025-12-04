def find_anagrams(word, candidates):
    response = []

    for candidate in candidates:
        if sorted(word.upper()) == sorted(candidate.upper()) and  word.upper() != candidate.upper():
            response.append(candidate)

    return response
    

    
