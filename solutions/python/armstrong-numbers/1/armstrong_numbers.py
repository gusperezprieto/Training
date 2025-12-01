def is_armstrong_number(number):
    
    strNumber = str(number)
    exp = len(strNumber)
    newNumber = 0

    for digit in strNumber:
        newNumber += int(digit) ** exp

    return number == newNumber
        
