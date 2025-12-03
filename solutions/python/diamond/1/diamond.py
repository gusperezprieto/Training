LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                      

def rows(letter):
    
    response = []
    index_letter = LETTERS.index(letter)

    for index in range(index_letter+1):
        string_ini = (index_letter - index)*" " + LETTERS[index] + (index)*" "
        
        print(string_ini)
        print(string_ini + string_ini[::-1][1:])
        response.append(string_ini + string_ini[::-1][1:])
      
    response = response + response[::-1][1:]
    return response
    
