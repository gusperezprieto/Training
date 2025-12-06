def roman(number):
    roman_number = ""

    thousands = number // 1000
    hundreds = (number % 1000)//100
    tens = (number % 100)//10
    units = number % 10

    roman_number = thousands * "M" + (hundreds//5)*"D" + (hundreds%5)*"C" + (tens//5)*"L" + (tens%5)*"X" + (units//5)*"V" + (units%5)*"I" 

    roman_number = roman_number.replace("DCCCC", "CM").replace("LXXXX", "XC").replace("VIIII", "IX")
    roman_number = roman_number.replace("CCCC", "CD").replace("XXXX", "XL").replace("IIII", "IV")

    return roman_number
    

