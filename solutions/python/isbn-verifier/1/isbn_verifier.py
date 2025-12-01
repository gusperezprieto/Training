def is_valid(isbn):
    isbn = isbn.replace("-","")

    if len(isbn) != 10:
        return False
    
    total = 0

    for index in range(9):
        if isbn[index].isalpha():
            return False
        total += int(isbn[index])*(10 - index)

    if isbn[9] == "X":
        total += 10
    elif isbn[9].isalpha():
        return False
    else:
        total += int(isbn[9])

        
    return total % 11 == 0
