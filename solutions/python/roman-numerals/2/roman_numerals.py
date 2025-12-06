def roman(number):
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    texts = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    res = []
    while number > 0:
        for index, val in enumerate(numbers):
            if (number >= val):
                res.append(texts[index])
                number -= val
                break; 

    return "".join(res)
        
    

